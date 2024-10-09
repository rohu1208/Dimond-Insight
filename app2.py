from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Get data from the request
            data = CustomData(
                carat=float(request.json.get('carat')),
                depth=float(request.json.get('depth')),
                table=float(request.json.get('table')),
                x=float(request.json.get('x')),
                y=float(request.json.get('y')),
                z=float(request.json.get('z')),
                cut=request.json.get('cut'),
                color=request.json.get('color'),
                clarity=request.json.get('clarity')
            )

            # Get the data as a DataFrame
            final_new_data = data.get_data_as_dataframe()

            # Prediction
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            # Prepare the response
            return jsonify(price=round(pred[0], 2))

        except Exception as e:
            # Print the error to the console for debugging
            print("Error during prediction:", str(e))
            return jsonify(error="Error predicting price. Please try again."), 500  # Internal Server Error

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
