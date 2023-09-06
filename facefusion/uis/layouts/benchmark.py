import gradio

from facefusion.uis.components import about, processors, execution, benchmark
from facefusion.utilities import conditional_download


def pre_check() -> bool:
	conditional_download('.assets/examples',
	[
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/source.jpg',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-240p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-360p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-540p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-720p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-1080p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-1440p.mp4',
		'https://github.com/facefusion/facefusion-assets/releases/download/examples/target-2160p.mp4'
	])
	return True


def render() -> gradio.Blocks:
	return layout


def listen() -> None:
	processors.listen()
	execution.listen()
	benchmark.listen()
