async function generatePassword() {
	const useCommon = document.getElementById('useCommon').checked;
	const response = await fetch(`/generate?use_common=${useCommon}`);
	const data = await response.json();
	document.getElementById('result').textContent = data.result;
}