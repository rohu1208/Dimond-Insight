from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline


application = Flask(__name__)  # Create a Flask application instance
app = application

@app.route('/')
def home_page():
    return render_template('template/index.html')  # Ensure this file existsy


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('template/form.html')  # Render the form for prediction
    else:
        try:
            # Get data from the form
            data = CustomData(
                carat=float(request.form.get('carat')),
                depth=float(request.form.get('depth')),
                table=float(request.form.get('table')),
                x=float(request.form.get('x')),
                y=float(request.form.get('y')),
                z=float(request.form.get('z')),
                cut=request.form.get('cut'),
                color=request.form.get('color'),
                clarity=request.form.get('clarity')
            )

            # Convert the data into a DataFrame for prediction
            final_new_data = data.get_data_as_dataframe()  # Assuming this method is implemented in CustomData

            # Create an instance of PredictPipeline
            predict_pipeline = PredictPipeline()

            # Make a prediction
            pred = predict_pipeline.predict(final_new_data)

            # Round the result to 2 decimal places
            results = round(pred[0], 2)

            return jsonify({'price': results})  # Return the result as JSON

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return error message in case of exception


if __name__ == '__main__':
    app.run(debug=True)
