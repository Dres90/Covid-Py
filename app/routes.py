from flask import render_template, url_for, request
from app import app
from app.models import Report, Date
from app.getReports import load_reports


@app.route('/')
@app.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    reports = Report.query.order_by(Report.name.asc()).paginate(
        page, app.config['REPORTS_PER_PAGE'], False)
    next_url = url_for('index', page=reports.next_num) \
        if reports.has_next else None
    prev_url = url_for('index', page=reports.prev_num) \
        if reports.has_prev else None
    updated = Date.query.get('lu').timestamp
    return render_template('index.html', title='Covid', reports=reports.items,
                           next_url=next_url, prev_url=prev_url,
                           updated=updated)


@app.route('/update')
def update():
    return render_template('update.html', message=load_reports())
