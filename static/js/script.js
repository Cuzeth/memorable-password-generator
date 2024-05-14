function toggleSlider(checked) {
	const slider = document.getElementById('leetifySlider');
	slider.style.display = checked ? 'block' : 'none';
}

function updateSliderValue(value) {
	document.getElementById('sliderValue').textContent = `${value}%`;
}

async function generatePassword() {
	const useCommon = document.getElementById('useCommon').checked;
	const leetify = document.getElementById('leetify').checked;
	const leetifyProbability = document.getElementById('leetifyProbability').value / 100;
	const response = await fetch(`/generate?use_common=${useCommon}&leetify=${leetify}&leetify_probability=${leetifyProbability}`);
	const data = await response.json();
	document.getElementById('result').textContent = data.result;
}
