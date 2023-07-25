from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST', 'GET'])
def plot_graph():
    if request.method == 'POST':
        print("Received POST request.")
        A = float(request.form['A'])
        w = float(request.form['w'])
        t = float(request.form['t'])
        k = float(request.form['k'])
        x = float(request.form['x'])

        # Create data for the graph
        time = np.linspace(0, t, 1000)
        wave = A * np.sin(w * time - k * x)

        # Generate the plot
        plt.figure(figsize=(8, 6))
        plt.plot(time, wave)
        plt.xlabel('Time (t)')
        plt.ylabel('Amplitude')
        plt.title('A * sin(wt - kx) Wave')
        plt.grid(True)

        # Save the plot to a BytesIO object and encode it to base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data = base64.b64encode(buffer.read()).decode('utf-8')

        # Close the plot
        plt.close()

            
        return render_template('index.html', plot_data=plot_data)
    
    print("Received GET request.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




        # ... (rest of the code for plotting the graph)


