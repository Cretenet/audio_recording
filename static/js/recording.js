var chunks = [];
var recorder;
var imput;
var audioContext;
let stream;
var recording = false;
var microphoneButton = document.getElementsByClassName("start-recording-button")[0];
var recordingContainer = document.getElementsByClassName("recording-contorl-buttons-container")[0];
var stopButton = document.getElementsByClassName("stop-recording-button")[0];
var navigationButtonPrev = document.getElementById("navigation_button_prev");
var navigationButtonNext = document.getElementById("navigation_button_next");
var change_page_button = document.getElementById("change_page_button");
// Listeners
microphoneButton.onclick = startRec;
stopButton.onclick = stopRec;
navigationButtonPrev.onclick = prevPage;
navigationButtonNext.onclick = nextPage;
change_page_button.onclick = changePage;

// Functions
function startRec() {
    chunks = [];
    recording = true;
    microphoneButton.style.display = "none";
    recordingContainer.style.display = "flex";
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            audioContext = new AudioContext();
            input = audioContext.createMediaStreamSource(stream);
            recorder = new WebAudioRecorder(input, {
                workerDir: static_url, // relative path to the WebAudioRecorder.js and WebAudioRecorderWav.min.js files
                encoding: 'wav',
                onEncoderLoading: function (recorder, encoding) {
                    console.log("Encoder loading: " + encoding);
                },
                onEncoderLoaded: function (recorder, encoding) {
                    console.log("Encoder loaded: " + encoding);
                },
                onTimeout: function (recorder) {
                    recorder.finishRecording();
                },
                onEncodingProgress: function (recorder, progress) {
                    console.log("Encoding Progress: " + progress);
                },
                onEncodingCanceled: function (recorder) {
                    console.log("Encoding cancelled");
                },
                onComplete: function (recorder, blob) {
                    chunks.push(blob);
                    let finalBlob = new Blob(chunks, { 'type': 'audio/wav' });
                    var number = document.getElementById('number').innerText;
                    if (!Number.isInteger(parseFloat(number))) {
                        var number = 0;
                    }
                    var csrftoken = document.querySelector('[name=csrf-token]').content;
                    let formData = new FormData();
                    formData.append('audio_file', finalBlob, 'audio.wav');
                    formData.append('number', number);
                    fetch('/record/upload_audio/', { method: 'POST', body: formData, headers: { 'X-CSRFToken': csrftoken } })
                        .then(response => response.json())
                        .then(data => {
                            document.querySelector('h3').textContent = data['sentence'];
                            document.querySelector('p').textContent = data['number'];
                        })
                        .catch((error) => console.error(error));
                    chunks = [];
                },
                onError: function (recorder, message) {
                    console.log("Error: " + message);
                }
            });
            recorder.setOptions({
                timeLimit: 300,
                encodeAfterRecord: true
            });
            recorder.startRecording();
        });
}


function stopRec() {
    recording = false;
    microphoneButton.style.display = "block";
    recordingContainer.style.display = "none";
    recorder.finishRecording();
    input.mediaStream.getTracks().forEach(track => track.stop());
}

document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        if (!recording) {
            startRec();
        } else {
            stopRec();
        }
    }
    else if (e.key === 'ArrowLeft') {
        prevPage();
    }
    else if (e.key === 'ArrowRight') {
        nextPage();
    }
});


function prevPage() {
    var number = document.getElementById('number').innerText;
    var csrftoken = document.querySelector('[name=csrf-token]').content;
    if (!Number.isInteger(parseFloat(number))) {
        var number = "1";
    }
    if (number != "1") {
        let formData = new FormData();
        formData.append('number', parseFloat(number) - 1);
        fetch('/record/go_to/', { method: 'POST', body: formData, headers: { 'X-CSRFToken': csrftoken } })
            .then(response => response.json())
            .then(data => {
                document.querySelector('h3').textContent = data['sentence'];
                document.querySelector('p').textContent = data['number'];
            })
            .catch((error) => console.error(error));
    }
};


function nextPage() {
    var number = document.getElementById('number').innerText;
    var csrftoken = document.querySelector('[name=csrf-token]').content;
    if (!Number.isInteger(parseFloat(number))) {
        var number = "1";
    }
    let formData = new FormData();
    formData.append('number', parseFloat(number) + 1);
    fetch('/record/go_to/', { method: 'POST', body: formData, headers: { 'X-CSRFToken': csrftoken } })
        .then(response => response.json())
        .then(data => {
            document.querySelector('h3').textContent = data['sentence'];
            document.querySelector('p').textContent = data['number'];
        })
        .catch((error) => console.error(error));
};

function changePage() {
    window.location.href = "/record/audio_list/";
};