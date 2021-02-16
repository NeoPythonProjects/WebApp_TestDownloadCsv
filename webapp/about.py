import justpy as jp


class About:
    path = "/about"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage()
        download_link = jp.A(a=wp, text="Download file About", href="/static/WAO_db_downloadtest.csv",
                             download="WAO_test_about.csv")
        # downloading the png below sometimes works
        # download_link = jp.A(a=wp, text="Download png file About", href="/static/house.png",
        #                      download="downloaded.png")
        return wp


if __name__ == "__main__":
    jp.Route(About.path, About.serve)
    jp.justpy(port=8001)
