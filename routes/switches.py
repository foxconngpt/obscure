
@bp.route('/')
def index():
    switches = Switch.query.all()
    return render_template('switches/index.html', switches=switches)

@bp.route('/executar_diagnostico', methods=['POST'])
def executar_diagnostico():
    return render_template('switches/diagnostico.html')

