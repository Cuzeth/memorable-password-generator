function toggleSlider(checked) {
	const slider = document.getElementById('leetifySlider');
	if (checked) {
		slider.classList.add('active');
	} else {
		slider.classList.remove('active');
	}
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
	const resultElement = document.getElementById('result');
	resultElement.textContent = data.result;
	resultElement.style.visibility = 'visible';
}

function toggleDarkMode() {
	const body = document.body;
	body.classList.toggle('dark-mode');
}
