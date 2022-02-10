import mode_sub as mm
import view

def button_clip():
    value_a = view.get_value()
    value_b = view.get_value()
    mm.init(value_a,value_b)
    result = mm.do_it()
    view.view_data(result,'result')