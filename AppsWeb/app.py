import web  

urls = (
    '/alumnos/?', 'AppsWeb.codigo.alumnos.AlumnosApi',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
