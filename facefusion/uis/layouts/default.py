import gradio

from facefusion.uis.components import about, processors, execution, temp_frame, settings, source, target, preview, trim_frame, face_analyser, face_selector, output_settings, output


def pre_check() -> bool:
	return True


def render() -> gradio.Blocks:
	return layout


def listen() -> None:
	processors.listen()
	execution.listen()
	settings.listen()
	temp_frame.listen()
	source.listen()
	target.listen()
	preview.listen()
	trim_frame.listen()
	face_selector.listen()
	face_analyser.listen()
	output_settings.listen()
	output.listen()
