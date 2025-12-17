
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from data import get_stretches

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mid-ride')
def mid_ride_filter():
    return render_template('filter.html')

@app.route('/stretches/<mode>')
def stretch_list(mode):
    filter_type = request.args.get('filter')
    stretches = get_stretches(mode, filter_type)
    
    mode_titles = {
        'pre': 'Pre-Ride (乗車前)',
        'mid': 'Mid-Ride (休憩中)',
        'post': 'Post-Ride (乗車後)'
    }
    
    title = mode_titles.get(mode, 'Stretches')
    if filter_type == 'discrete':
        title += ' - コンビニ/人前'
    elif filter_type == 'active':
        title += ' - 公園/広い場所'
        
    return render_template('list.html', stretches=stretches, title=title, mode=mode)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
