from tkinter import *

class GUI:
    '''
    A class to representing the GUI object
    '''

    def __init__(self, window)->None:
        """
        Method to set the interface of the primary window and commands that directed through buttons.
        """
        self.window = window
        #Status
        self.frame_shapes = Frame(self.window)
        self.label_shapes = Label(self.frame_shapes, text='Areas of Shapes')
        self.label_shapes.pack(padx=45, side='left')
        self.frame_shapes.pack(anchor='w', pady=20)

        self.radio_rectangle = Button(self.frame_shapes, text='RECTANGLE', padx=10, pady=5, command=self.click_rectangle)
        self.radio_square = Button(self.frame_shapes, text='SQUARE', padx=10, pady=5, command=self.click_square)
        self.radio_triangle = Button(self.frame_shapes, text='TRIANGLE', padx=10, pady=5, command=self.click_triangle)
        self.radio_circle = Button(self.frame_shapes, text='CIRCLE', padx=10, pady=5, command=self.click_circle)
        self.radio_rectangle.pack(side='right')
        self.radio_square.pack(side='right')
        self.radio_circle.pack(side='right')
        self.radio_triangle.pack(side='right')
        self.frame_shapes.pack()
        #Save
        self.button_submit = Button(self.window, text='EXIT', padx=10, pady=5, command=window.destroy)
        self.button_submit.pack(side='bottom', pady=20)

    def click_triangle(self) -> None:
        '''
        Method to calculate float data for the area of a triangle.
        '''
        top_triangle = Toplevel()
        top_triangle.title('Area of a Triangle')
        top_triangle.geometry('300x350')
        top_triangle.resizable(False, False)

        triangle_label = Label(top_triangle, text='Enter Triangle Measurements')
        triangle_label.pack(pady=25)

        def triangle_number_validation()->None:
            '''
            A Method to Validate data is entered as float data.
            '''
            try:
                height = float(triangle_height_box.get())
                base = float(triangle_base_box.get())
                if base > 0 and height > 0:
                    triangle_answer = (base * height)/2
                    answer.config(text='Area of the Triangle: '+ format(triangle_answer, '.2f'))
                else:
                    answer.config(text='Please enter positive numbers.')
            except ValueError:
                answer.config(text='Please enter numbers.')

        triangle_height_label = Label(top_triangle, text='Enter Height of the Triangle: ')
        triangle_height_label.pack(pady=5)

        triangle_height_box = Entry(top_triangle)
        triangle_height_box.pack(padx=10, pady=10)

        triangle_base_label = Label(top_triangle, text='Enter Base of the Triangle: ')
        triangle_base_label.pack(pady=5)

        triangle_base_box = Entry(top_triangle)
        triangle_base_box.pack(padx=10, pady=10)

        answer = Label(top_triangle, text='')
        answer.pack(pady=25)

        circle_execution = Button(top_triangle, text='Execute', command=triangle_number_validation)
        circle_execution.pack(pady=10)

    def click_circle(self)->None:
        '''
        Method to calculate float data for the area of a circle.
        '''
        top_circle = Toplevel()
        top_circle.title('Area of a Circle')
        top_circle.geometry('300x350')
        top_circle.resizable(False, False)

        circle_label = Label(top_circle, text='Enter Circle Measurements')
        circle_label.pack(pady=40)

        def circle_number_validation()->None:
            '''
            A Method to validate data is entered as float data.
            '''
            try:
                radius = float(circle_radius_box.get())
                if radius > 0:
                    circle_answer = radius * radius
                    answer.config(text='Area of the Circle: '+ format(circle_answer, '.2f'))
                else:
                    answer.config(text='Please enter positive numbers.')
            except ValueError:
                answer.config(text='Please enter numbers.')

        circle_radius_label = Label(top_circle, text='Enter Radius of the Circle: ')
        circle_radius_label.pack(pady=5)

        circle_radius_box = Entry(top_circle)
        circle_radius_box.pack(padx=10, pady=20)

        answer = Label(top_circle, text='')
        answer.pack(pady=20)

        circle_execution = Button(top_circle, text='Execute', command=circle_number_validation)
        circle_execution.pack(pady=20)

    def click_square(self)->None:
        '''
        Method to calculate float data for the area of a square.
        '''
        top_square = Toplevel()
        top_square.title('Area of a Square')
        top_square.geometry('300x350')
        top_square.resizable(False, False)

        square_label = Label(top_square, text='Enter Square Measurements')
        square_label.pack(pady=40)

        def square_number_validation()->None:
            '''
            A Method to Validate data is entered as float data.
            '''
            try:
                length = float(square_length_box.get())
                if length > 0:
                    square_answer = length * 2
                    answer.config(text='Area of the Square: '+ format(square_answer, '.2f'))
                else:
                    answer.config(text='Please enter a positive number.')
            except ValueError:
                answer.config(text='Please enter a number.')

        square_length_label = Label(top_square, text='Enter Length of the Square: ')
        square_length_label.pack(pady=5)

        square_length_box = Entry(top_square)
        square_length_box.pack(padx=10, pady=20)

        answer = Label(top_square, text='')
        answer.pack(pady=20)

        square_execution = Button(top_square, text='Execute', command=square_number_validation)
        square_execution.pack(pady=20)

    def click_rectangle(self)->None:
        '''
        Method to calculate float data for the area of a rectangle.
        '''
        top_rectangle = Toplevel()
        top_rectangle.title('Area of a Rectangle')
        top_rectangle.geometry('300x350')
        top_rectangle.resizable(False, False)

        rectangle_label = Label(top_rectangle, text='Enter Rectangle Measurements')
        rectangle_label.pack(pady=25)

        def rectangle_number_validation()->None:
            '''
            A Method to Validate data is entered as float data.
            '''
            try:
                length = float(rectangle_length_box.get())
                width = float(rectangle_width_box.get())
                if length > 0 and width > 0:
                    rectangle_answer = length * width
                    answer.config(text='Area of the Rectangle: '+ format(rectangle_answer, '.2f'))
                else:
                    answer.config(text='Please enter positive numbers.')
            except ValueError:
                answer.config(text='Please enter numbers.')

        rectangle_length_label = Label(top_rectangle, text='Enter Length of the Rectangle: ')
        rectangle_length_label.pack(pady=5)

        rectangle_length_box = Entry(top_rectangle)
        rectangle_length_box.pack(padx=10, pady=10)

        rectangle_width_label = Label(top_rectangle, text='Enter Width of the Rectangle: ')
        rectangle_width_label.pack(pady=5)

        rectangle_width_box = Entry(top_rectangle)
        rectangle_width_box.pack(padx=10, pady=10)

        answer = Label(top_rectangle, text='')
        answer.pack(pady=20)

        circle_execution = Button(top_rectangle, text='Execute', command=rectangle_number_validation)
        circle_execution.pack(pady=15)
