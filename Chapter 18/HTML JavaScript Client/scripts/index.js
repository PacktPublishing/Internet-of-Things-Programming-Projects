function moveForward() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendMoveForwardMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendMoveForwardMessage() {
    message = new Paho.MQTT.Message("Forward");
    message.destinationName = "RobotControl";
    client.send(message);
}

function moveBackward() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendMoveBackwardMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendMoveBackwardMessage() {
    message = new Paho.MQTT.Message("Backward");
    message.destinationName = "RobotControl";
    client.send(message);
}

function turnLeft() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendTurnLeftMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendTurnLeftMessage() {
    message = new Paho.MQTT.Message("Left");
    message.destinationName = "RobotControl";
    client.send(message);
}

function turnRight() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendTurnRightMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendTurnRightMessage() {
    message = new Paho.MQTT.Message("Right");
    message.destinationName = "RobotControl";
    client.send(message);
}

function takePicture() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendTakePictureMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendTakePictureMessage() {
    message = new Paho.MQTT.Message("Picture");
    message.destinationName = "RobotControl";
    client.send(message);
}

function TARASAlarm() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: sendTARASAlarmMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function sendTARASAlarmMessage() {
    message = new Paho.MQTT.Message("Alarm");
    message.destinationName = "RobotControl";
    client.send(message);
}

function makeTARASDance() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: makeTARASDanceMessage,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}

// called when the client connects
function makeTARASDanceMessage() {
    message = new Paho.MQTT.Message("Dance");
    message.destinationName = "RobotControl";
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

function onsubsribeDistanceDataSuccess() {
    client.subscribe("distance");
    alert("Subscribed to distance data");
}

function subscribeDistanceData() {
    client = new Paho.MQTT.Client("m10.cloudmqtt.com", 38215, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;
    var options = {
        useSSL: true,
        userName: "vectydkb",
        password: "ZpiPufitxnnT",
        onSuccess: onsubsribeDistanceDataSuccess,
        onFailure: doFail
    }

    // connect the client
    client.connect(options);
}