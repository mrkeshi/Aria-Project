// src/firebase.js

import { initializeApp } from "firebase/app";
import { getMessaging, getToken, onMessage } from "firebase/messaging";

const firebaseConfig = {
  apiKey: "AIzaSyAMAtt-W0-Py4cBvfQ7YVdMFBGsydI9y1c",
  authDomain: "aria-11cbb.firebaseapp.com",
  projectId: "aria-11cbb",
  storageBucket: "aria-11cbb.appspot.com",
  messagingSenderId: "1071435067795",
  appId: "1:1071435067795:web:fe48ee06a9ca73297bf866",
  measurementId: "G-6Q9TYRNYTP"
};

const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);

export const requestFirebaseNotificationPermission = async () => {
  const permission = Notification.permission;

  try {
    if (permission === 'granted') {
      const token = await getToken(messaging, {
        vapidKey: "BNT80fpa0SJpLo2753bTSbkyL-lXrl0YO1RlTqHVHipH_IMOK7SKYRD-zTXMzVhdWzv4x_l-7Tw9aHlekz8MpL4"
      });
      console.log("🔔 Token received:", token);
      return token;
    }

    if (permission === 'default') {
      const result = await Notification.requestPermission();
      if (result === 'granted') {
        const token = await getToken(messaging, {
          vapidKey: "BNT80fpa0SJpLo2753bTSbkyL-lXrl0YO1RlTqHVHipH_IMOK7SKYRD-zTXMzVhdWzv4x_l-7Tw9aHlekz8MpL4"
        });
        console.log("🔔 Token received after request:", token);
        return token;
      } else {
        throw new Error('Notification permission was denied by user.');
      }
    }

    if (permission === 'denied') {
      throw new Error('Notification permission was blocked in browser settings.');
    }

  } catch (err) {
    console.error("❌ An error occurred while retrieving token:", err);
    throw err;
  }
};

export const onMessageListener = () =>
  new Promise((resolve) => {
    onMessage(messaging, (payload) => {
      console.log("📩 Message received: ", payload);
      resolve(payload);
    });
  });
