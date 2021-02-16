import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage()
        div = jp.Div(a=wp, text="main div", classes="text=lg p-2 m-2")
        jp.Br(a=wp)
        jp.A(a=div, text="link to about", href="/about")
        return wp

# this is triggered when you type /farms, this is a Get request??
# jp.Route(Home.path, Home.serve)
# jp.justpy(port=8000)