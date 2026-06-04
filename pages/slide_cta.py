import dash
from dash import html
import dash_bootstrap_components as dbc
from pages.components import sidebar

dash.register_page(__name__, path='/slide_cta')


_VALUE_METRICS = [
    {
        'value': 'R²=0.59',
        'label': 'Digitalización → Salarios',
        'color': '#00b87a',
        'class': 'card-success',
    },
    {
        'value': 'R²=0.45',
        'label': 'Digitalización → Percepción de seguridad',
        'color': '#00b4cc',
        'class': 'card-cyan',
    },
    {
        'value': 'r=+0.78',
        'label': 'Digitalización → Confianza social',
        'color': '#c9922a',
        'class': 'card-gold',
    },
]

_CONCLUSIONS = [
    (
        '01',
        'Crecimiento económico',
        'Los estados más digitalizados presentan mejores salarios y mayor inclusión financiera.',
        'La hoja de economía muestra R²=0.594 entre banca digital y salarios. Además, el análisis de rezagos indica que el efecto más fuerte aparece dos años después de invertir.',
        '#00b87a',
    ),
    (
        '02',
        'Capital social',
        'La confianza ciudadana aumenta conforme mejora la infraestructura digital.',
        'La hoja de percepción encuentra R²≈0.445 entre IDDE y seguridad percibida, y el análisis de confianza reporta r=+0.78 entre cobertura digital y confianza social.',
        '#00b4cc',
    ),
    (
        '03',
        'Retorno sostenible',
        'La consistencia en la inversión importa más que el gasto puntual.',
        'El resultado de inversión sostenida compara estados que mejoran IDDE de forma consistente: ahí aparecen retornos salariales mayores que en aumentos aislados.',
        '#c9922a',
    ),
]

_METHOD_STEPS = [
    (
        'Datos cruzados',
        'Se integran IDDE, ENOE, ENVIPE, incidencia delictiva, DENUE y variables económicas por estado.',
        '#00b4cc',
    ),
    (
        'Relaciones medidas',
        'Se comparan correlaciones, R², rezagos y perfiles K-Means para separar economía, percepción, crimen y ciberseguridad.',
        '#00b87a',
    ),
    (
        'Lectura conjunta',
        'Las señales convergen: salario, percepción y confianza suben con digitalización; fraude también, por eso aparece la capa de protección.',
        '#c9922a',
    ),
]

_PROTECTION_SIGNALS = [
    ('r=+0.63', 'Fraude y digitalización', '#c9922a'),
    ('8 estados', 'Brecha crítica de ciberseguridad', '#cf0a2c'),
    ('r≈0', 'Relación entre IDDE y homicidio', '#00b4cc'),
]

_CAPABILITIES = [
    (
        'Conectividad',
        'Expandir acceso y cobertura digital.',
        'El dashboard separa cobertura, velocidad y banca digital: la calidad de conexión y la adopción financiera son las variables que más se traducen en salario y uso.',
    ),
    (
        'Gobernanza',
        'Incrementar confianza y adopción ciudadana.',
        'La evidencia de percepción muestra que digitalizar no basta: la adopción depende de confianza ciudadana, servicios útiles y capacidad institucional visible.',
    ),
    (
        'Ciberseguridad',
        'Reducir vulnerabilidades y fraude digital.',
        'Fraude es el delito con mayor asociación al IDDE (r=+0.63); por eso el crecimiento digital debe acompañarse de antifraude y monitoreo.',
    ),
    (
        'Datos e inteligencia',
        'Convertir infraestructura en decisiones públicas más efectivas.',
        'Los clusters y el perfil por estado muestran que no todos necesitan lo mismo: los datos permiten priorizar brechas, riesgo y retorno esperado.',
    ),
]


def _metric_card(metric, delay=''):
    return dbc.Col(
        dbc.Card([
            dbc.CardBody([
                html.P(metric['value'], style={
                    'fontFamily': 'DM Mono, monospace',
                    'fontSize': '30px',
                    'fontWeight': '800',
                    'color': metric['color'],
                    'lineHeight': '1',
                    'marginBottom': '12px',
                }),
                html.P(metric['label'], style={
                    'fontSize': '13px',
                    'fontWeight': '700',
                    'color': '#e8e8f0',
                    'lineHeight': '1.35',
                    'margin': '0',
                }),
            ], style={'padding': '22px 24px'}),
        ], className=f"animate-in h-100 {metric['class']} {delay}".strip()),
        md=4,
    )


def _conclusion_card(num, title, text, rationale, color, delay=''):
    return dbc.Col(
        html.Div([
            html.Div(num, style={
                'fontFamily': 'DM Mono, monospace',
                'fontSize': '24px',
                'fontWeight': '800',
                'color': color,
                'marginBottom': '18px',
            }),
            html.H3(title, style={
                'fontSize': '17px',
                'fontWeight': '700',
                'color': '#e8e8f0',
                'marginBottom': '9px',
            }),
            html.P(text, style={
                'fontSize': '12.5px',
                'color': '#b8b8cc',
                'lineHeight': '1.65',
                'marginBottom': '12px',
            }),
            html.P(rationale, style={
                'fontSize': '11px',
                'color': '#9090a8',
                'lineHeight': '1.55',
                'margin': '0',
                'paddingTop': '10px',
                'borderTop': f'1px solid {color}30',
            }),
        ], className=f'animate-in {delay}'.strip(), style={
            'height': '100%',
            'padding': '24px 22px',
            'border': f'1px solid {color}33',
            'borderTop': f'3px solid {color}',
            'borderRadius': '8px',
            'background': (
                f'linear-gradient(180deg, {color}12 0%, '
                'rgba(255,255,255,0.018) 56%, rgba(255,255,255,0.01) 100%)'
            ),
        }),
        md=4,
    )


def _method_card(title, text, color, delay=''):
    return dbc.Col(
        html.Div([
            html.Div(style={
                'width': '24px',
                'height': '2px',
                'borderRadius': '2px',
                'background': color,
                'marginBottom': '10px',
            }),
            html.P(title, style={
                'fontSize': '10px',
                'fontWeight': '800',
                'letterSpacing': '0.10em',
                'textTransform': 'uppercase',
                'color': color,
                'marginBottom': '7px',
            }),
            html.P(text, style={
                'fontSize': '11.5px',
                'color': '#b8b8cc',
                'lineHeight': '1.55',
                'margin': '0',
            }),
        ], className=f'animate-in {delay}'.strip(), style={
            'height': '100%',
            'padding': '15px 16px',
            'border': f'1px solid {color}26',
            'background': f'linear-gradient(180deg, {color}10, rgba(255,255,255,0.012))',
            'borderRadius': '8px',
        }),
        md=4,
    )


def _signal(value, label, color):
    return html.Div([
        html.Span(value, style={
            'display': 'block',
            'fontFamily': 'DM Mono, monospace',
            'fontSize': '17px',
            'fontWeight': '800',
            'color': color,
            'marginBottom': '4px',
        }),
        html.Span(label, style={
            'display': 'block',
            'fontSize': '10.5px',
            'fontWeight': '600',
            'color': '#c4c4d4',
            'lineHeight': '1.35',
        }),
    ], style={
        'padding': '13px 14px',
        'borderLeft': f'2px solid {color}',
        'background': f'{color}0f',
        'borderRadius': '6px',
        'height': '100%',
    })


def _capability(num, title, text, rationale):
    return dbc.Col(
        html.Div([
            html.Span(f'{num:02d}', style={
                'fontFamily': 'DM Mono, monospace',
                'fontSize': '11px',
                'fontWeight': '800',
                'color': '#5c5c74',
                'marginRight': '10px',
            }),
            html.Div([
                html.P(title, style={
                    'fontSize': '12px',
                    'fontWeight': '700',
                    'color': '#e8e8f0',
                    'margin': '0 0 3px',
                }),
                html.P(text, style={
                    'fontSize': '10.5px',
                    'color': '#9090a8',
                    'lineHeight': '1.45',
                    'marginBottom': '6px',
                }),
                html.P(rationale, style={
                    'fontSize': '10px',
                    'color': '#6f6f88',
                    'lineHeight': '1.45',
                    'margin': '0',
                }),
            ]),
        ], style={
            'display': 'flex',
            'alignItems': 'flex-start',
            'height': '100%',
            'padding': '12px 8px',
        }),
        md=3,
    )


layout = html.Div([
    sidebar('/slide_cta'),

    html.Div([
        html.Div([
            html.Div(className='page-accent-line'),
            html.H1('Conclusiones', className='page-title'),
            html.P(
                'La infraestructura digital genera valor económico y social',
                className='page-subtitle',
            ),
            html.Div([
                html.Span('Valor económico', className='badge-green me-2'),
                html.Span('Confianza social', className='badge-cyan me-2'),
                html.Span('Protección digital', className='badge-gold'),
            ]),
        ], className='page-header'),

        html.Div([
            dbc.Row([
                _metric_card(_VALUE_METRICS[0]),
                _metric_card(_VALUE_METRICS[1], 'animate-in-delay-1'),
                _metric_card(_VALUE_METRICS[2], 'animate-in-delay-2'),
            ], className='g-3 mb-4'),

            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Div([
                            html.Div(className='section-accent-cyan'),
                            html.H3('Cómo se llega a estas conclusiones',
                                    className='section-block-title'),
                        ]),
                        html.P(
                            'El dashboard cruza indicadores de digitalización con resultados sociales, '
                            'económicos y de seguridad para identificar patrones consistentes, no casos aislados.',
                            style={
                                'fontSize': '12.5px',
                                'color': '#9a9ab5',
                                'lineHeight': '1.55',
                                'margin': '0',
                                'maxWidth': '620px',
                            },
                        ),
                    ], style={
                        'display': 'flex',
                        'justifyContent': 'space-between',
                        'gap': '18px',
                        'alignItems': 'flex-end',
                        'marginBottom': '14px',
                    }),
                    dbc.Row([
                        _method_card(*_METHOD_STEPS[0]),
                        _method_card(*_METHOD_STEPS[1], 'animate-in-delay-1'),
                        _method_card(*_METHOD_STEPS[2], 'animate-in-delay-2'),
                    ], className='g-2'),
                ], style={'padding': '20px 22px'}),
            ], className='card-clean animate-in mb-4'),

            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P('El hallazgo principal', style={
                                'fontSize': '10px',
                                'fontWeight': '800',
                                'letterSpacing': '0.12em',
                                'textTransform': 'uppercase',
                                'color': '#00d98f',
                                'marginBottom': '12px',
                            }),
                            html.H2(
                                'Digitalizar crea crecimiento, confianza y seguridad percibida.',
                                style={
                                    'fontSize': '28px',
                                    'fontWeight': '700',
                                    'color': '#e8e8f0',
                                    'lineHeight': '1.18',
                                    'marginBottom': '0',
                                },
                            ),
                        ], md=5),
                        dbc.Col([
                            html.P(
                                'La infraestructura digital no solo mejora la conectividad: '
                                'también incrementa ingresos, fortalece la confianza ciudadana '
                                'y mejora la percepción de seguridad.',
                                style={
                                    'fontSize': '15px',
                                    'color': '#c4c4d4',
                                    'lineHeight': '1.68',
                                    'marginBottom': '14px',
                                },
                            ),
                            html.P(
                                'Los beneficios más importantes aparecen después de dos años, '
                                'por lo que la inversión debe evaluarse con visión de mediano plazo.',
                                style={
                                    'fontSize': '15px',
                                    'fontWeight': '600',
                                    'color': '#e8e8f0',
                                    'lineHeight': '1.65',
                                    'margin': '0',
                                },
                            ),
                        ], md=7),
                    ], className='align-items-center'),
                ], style={'padding': '32px'}),
            ], className='card-clean animate-in mb-4', style={
                'borderLeft': '4px solid #00b87a66',
            }),

            dbc.Row([
                _conclusion_card(*_CONCLUSIONS[0]),
                _conclusion_card(*_CONCLUSIONS[1], 'animate-in-delay-1'),
                _conclusion_card(*_CONCLUSIONS[2], 'animate-in-delay-2'),
            ], className='g-3 mb-4'),

            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Div(className='section-accent-cyan'),
                            html.H3('Digitalizar sí, pero con protección',
                                    className='section-block-title'),
                            html.P(
                                'Más conectividad, banca digital y comercio electrónico generan crecimiento, '
                                'pero también amplían la superficie de ataque. La siguiente etapa no es solo '
                                'desplegar más tecnología: es construir capacidades de ciberseguridad que '
                                'permitan sostener ese crecimiento.',
                                style={
                                    'fontSize': '12.5px',
                                    'color': '#b8b8cc',
                                    'lineHeight': '1.65',
                                    'margin': '0',
                                },
                            ),
                        ], md=5),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(_signal(*_PROTECTION_SIGNALS[0]), md=4),
                                dbc.Col(_signal(*_PROTECTION_SIGNALS[1]), md=4),
                                dbc.Col(_signal(*_PROTECTION_SIGNALS[2]), md=4),
                            ], className='g-2 mb-3'),
                            dbc.Row([
                                _capability(i + 1, title, text, rationale)
                                for i, (title, text, rationale) in enumerate(_CAPABILITIES)
                            ], className='g-1'),
                        ], md=7),
                    ], className='g-3 align-items-stretch'),
                ], style={'padding': '24px 26px'}),
            ], className='card-clean animate-in mb-4'),
        ], className='main-scroll'),
    ], className='main-content'),
], className='page-root')
