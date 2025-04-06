from setuptools import setup, find_packages

setup(
    name="icse-question-generator",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'icse_question_generator': ['templates/*', 'static/*'],
    },
    install_requires=[
        "Flask==3.0.2",
        "gunicorn==21.2.0",
        "Werkzeug==3.0.1",
        "python-dotenv==1.0.1",
        "click==8.1.7",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3"
    ],
    python_requires='>=3.11.0',
) 