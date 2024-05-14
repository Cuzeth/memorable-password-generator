async function generatePassword() {
	const useCommon = document.getElementById('useCommon').checked;
	const leetify = document.getElementById('leetify').checked;
	const response = await fetch(`/generate?use_common=${useCommon}&leetify=${leetify}`);
	const data = await response.json();
	document.getElementById('result').textContent = data.result;
}
