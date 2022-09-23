from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape

from variables import about as aboutUs


class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()
        elif self.path == '/blog':
            self.render_blog()
        elif self.path == '/contact':
            self.render_contact()
        elif self.path == '/blog-single':
            self.render_blog_single()
        elif self.path == '/gallery':
            self.render_gallery()
        elif self.path == '/schedule':
            self.render_schedule()
        elif self.path == '/about':
            self.render_about()

    def render_index(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('index.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_blog(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('blog.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_contact(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('contact.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_blog_single(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('blog-single.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_gallery(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('gallery.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_schedule(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('schedule.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_about(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        body = self.env.get_template('about-us.html').render(listTrainer=aboutUs.list_trainer)
        print(body)
        self.wfile.write(body.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Server starting')
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=CustomHandler)