# Hola 3    -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# Platzi 4  -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puede utilizar cadenas"
        return string*n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))

if __name__ == "__main__":
    run()