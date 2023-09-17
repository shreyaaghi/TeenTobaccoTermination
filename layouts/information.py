from PIL import Image
import PySimpleGUI as gui
import io
import os
from util import get_config

# load_image("images/refusal.png", window, "img")

config = get_config()
width, height = config['width'], config['height']

def information():
    font = {"Helvetica", 25}
    layout = [
        [gui.Button("Back", key="Information Back Button"), gui.Text("Information", font={"Helvetica",25})],
        [gui.Multiline("According to the National Cancer Institute, over 90% of daily adult cigarette smokers began smoking before the age of 18. This striking statistic highlights a deeply concerning trend: smoking among teenagers. What might seem like a harmless experiment or a brief habit can have extreme consequences for both health and well-being. By the time young adults are introduced to smoking, it can be too late. The best way to prevent the road down to addiction is to learn about it at an earlier age. In this section, we'll dive into the world of tobacco use among teenagers by exploring the factors that contribute to this behavior and the risks that come with it. By gaining insight into the reasons behind these choices and the potential impact on young lives, the goal is to help both teenagers and those who care about them to make informed decisions.", key="introText", write_only = True, font={"Helvetica",13}, size = (width//20, 20)), gui.Image(key="img")], # TODO Set the size of multline. It technically already works?
        [gui.Text("What is a Cigarette?", font={"Helvetica",13, "bold"})]
    ]
    return layout