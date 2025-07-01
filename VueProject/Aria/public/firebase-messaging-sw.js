importScripts("https://www.gstatic.com/firebasejs/10.12.1/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/10.12.1/firebase-messaging-compat.js");

firebase.initializeApp({
  apiKey: "AIzaSyAMAtt-W0-Py4cBvfQ7YVdMFBGsydI9y1c",
  authDomain: "aria-11cbb.firebaseapp.com",
  projectId: "aria-11cbb",
  storageBucket: "aria-11cbb.appspot.com",
  messagingSenderId: "1071435067795",
  appId: "1:1071435067795:web:fe48ee06a9ca73297bf866",
  measurementId: "G-6Q9TYRNYTP"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function (payload) {
  console.log("Received background message ", payload);

  const { title, ...options } = payload.notification;
  self.registration.showNotification(title, options);
});
