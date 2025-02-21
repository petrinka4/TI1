async function encryptColumnMethod() {
    const keyToEncrypt = document.getElementById('inputFieldColumn').value;  
    const fileInput = document.getElementById('fileInputColumn');  
    const isEncrypt = document.getElementById("encryptCheckboxColumn").checked;  

    if (fileInput.files.length === 0) {
        alert("Выберите файл!");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("key", keyToEncrypt);
    formData.append("input_file", file);

    console.log("Отправка данных:");
    console.log("Ключ:", keyToEncrypt);
    console.log("Файл:", file);
    console.log("Режим:", isEncrypt ? "Шифрование" : "Расшифрование");

    const url = isEncrypt ? 'http://127.0.0.1:8000/encrypt/column' : 'http://127.0.0.1:8000/decrypt/column';

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData  
        });

        if (!response.ok) {
            alert("Ошибка при отправке файла: " + response.statusText);
            return;
        }

        const result = await response.json();
        document.getElementById("outputFieldColumn").textContent = result.result;  

    } catch (error) {
        alert("Ошибка при отправке запроса: " + error);
    }
}

async function encryptVigenereMethod() {
    const keyToEncrypt = document.getElementById('inputFieldVigenere').value;
    const fileInput = document.getElementById('fileInputVigenere');
    const isEncrypt = document.getElementById("encryptCheckboxVigenere").checked;

    if (fileInput.files.length === 0) {
        alert("Выберите файл!");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("key", keyToEncrypt);
    formData.append("input_file", file);

    console.log("Отправка данных:");
    console.log("Ключ:", keyToEncrypt);
    console.log("Файл:", file);
    console.log("Режим:", isEncrypt ? "Шифрование" : "Расшифрование");

    const url = isEncrypt ? 'http://127.0.0.1:8000/encrypt/vigenere' : 'http://127.0.0.1:8000/decrypt/vigenere';

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData  
        });

        if (!response.ok) {
            alert("Ошибка при отправке файла: " + response.statusText);
            return;
        }

        const result = await response.json();
        document.getElementById("outputFieldVigenere").textContent = result.result;

    } catch (error) {
        alert("Ошибка при отправке запроса: " + error);
    }
}
