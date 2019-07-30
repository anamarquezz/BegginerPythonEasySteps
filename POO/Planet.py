class Planet: #Calling methods inside method from the same Class
    def rotate(selft):
        print("rotate")

    def revolve(self):
        print("revolve")

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()


earth = Planet()
earth.rotate_and_revolve()
