from src.fractal_gen import draw

conf1 = {
    "string":"F+F+F+F",
    "rules":{
        "F": "F+F-F-FF+F+F-F+F+F+F-F"
    },
    "distance": 5,
    "angle": 90.0,
    "deepth": 4
}

def main():
    draw(**conf1)

if __name__ == "__main__":
    main()
