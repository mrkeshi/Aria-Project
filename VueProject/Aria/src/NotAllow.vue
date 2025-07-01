<template>
  <div v-if="showPermissionDialog">
    <div class="overlay"></div>
    <div class="permission-dialog">
      <p>آیا مایل هستید اعلان‌های مربوط به وظایف خود را دریافت کنید؟</p>
      <div class="buttons">
        <button class="green" @click="askNotificationPermission">بله</button>
        <button class="red" @click="dismiss">خیر</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const showPermissionDialog = ref(true);
const oneSignalLoaded = ref(false);

onMounted(() => {
  // بارگذاری SDK فقط یک بار
  if (!window.OneSignal) {
    const script = document.createElement("script");
    script.src = "https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js";
    script.async = true;
    script.onload = initOneSignal;
    document.head.appendChild(script);
  } else {
    initOneSignal();
  }
});

function initOneSignal() {
  window.OneSignal = window.OneSignal || [];
  const OneSignal = window.OneSignal;

  OneSignal.push(function () {
    OneSignal.init({
      appId: "f5669b06-a3c7-4dbb-90be-94b14ae50a97",
      allowLocalhostAsSecureOrigin: true,
      serviceWorkerPath: "/OneSignalSDKWorker.js",
      serviceWorkerUpdaterPath: "/OneSignalSDKUpdaterWorker.js",
    });

    oneSignalLoaded.value = true;
  });
}

async function askNotificationPermission() {
  if (!oneSignalLoaded.value) return;

  const OneSignal = window.OneSignal;

  OneSignal.push(async function () {
    const isEnabled = await OneSignal.isPushNotificationsEnabled();
    if (isEnabled) {
      showPermissionDialog.value = false;
      getUserId();
    } else {
      try {
        await OneSignal.showSlidedownPrompt();
        showPermissionDialog.value = false;
        getUserId();
      } catch (e) {
        console.log("User denied notification permission or error:", e);
        showPermissionDialog.value = false;
      }
    }
  });
}

function getUserId() {
  const OneSignal = window.OneSignal;
  OneSignal.getUserId().then((userId) => {
    console.log("OneSignal User ID:", userId);
  });
}

function dismiss() {
  showPermissionDialog.value = false;
  console.log("User dismissed the permission prompt");
}
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(6px);
  z-index: 9998;
}

.permission-dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  padding: 24px 32px;
  text-align: right;
  direction: rtl;
  width: 90%;
  max-width: 400px;
  font-size: 1.1rem;
  z-index: 9999;
}

.buttons {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

button {
  padding: 8px 16px;
  border: none;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button.green {
  background-color: #4caf50;
}

button.green:hover {
  background-color: #388e3c;
}

button.red {
  background-color: #f44336;
}

button.red:hover {
  background-color: #d32f2f;
}
</style>
