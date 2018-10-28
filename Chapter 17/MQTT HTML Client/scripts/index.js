function sendTestData() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendTestDataMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendTestDataMessage() {
    message = new Paho.MQTT.Message("Hello from JavaScript client");
    message.destinationName = "test";
    client.send(message);
}

function doFail() {
    alert("Error!");
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        alert("onConnectionLost:" + responseObject.errorMessage);
    }
}

// called when a message arrives
function onMessageArrived(message) {
    document.getElementById('messageTxt').value = message.payloadString; 
}

function onsubsribeTestDataSuccess() {
    client.subscribe("test");
    alert("Subscribed to test");
}

function subscribeTestData() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: onsubsribeTestDataSuccess,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}