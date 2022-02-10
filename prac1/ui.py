import data_provider as dp
import loger as log

def temperature_view(sensor):
    data = dp.get_temperature(sensor)
    log.temperature_logger(data)
    return data

def pressure_view(sensor):
    data = dp.get_preassure(sensor)
    log.preassure_logger(data)
    return data

def wind_view(sensor):
    data = dp.get_wind_speed(sensor)
    log.wind_speed_logger(data)
    return data