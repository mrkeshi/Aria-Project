<template>
  <div v-if="showPermissionDialog">
    <div class="overlay"></div>
    <div class="permission-dialog">
      <div v-if="showGuide">
        <p>لطفا از منوی سمت چپ گزینه <strong>فعال‌سازی</strong> را کلیک کنید.</p>
        <div class="loading"></div>
      </div>

      <div v-else>
        <p>آیا مایل هستید اعلان‌های مربوط به وظایف خود را دریافت کنید؟</p>
        <div class="buttons">
          <button class="green" @click="requestPermission">بله</button>
          <button class="red" @click="dismiss">خیر</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useNotificationStore } from "@/stores/notificationStore";
import { useAuthStore } from "@/stores/auth";
import { onMounted } from "vue";
const showPermissionDialog = ref(false);
const showGuide = ref(false);

const notification = useNotificationStore();
const auth = useAuthStore();

onMounted(() => {
  if (Notification.permission === "default") {
    showPermissionDialog.value = true;
  }
});

async function requestPermission() {
  if (!("Notification" in window)) {
    alert("این مرورگر از اعلان پشتیبانی نمی‌کند.");
    showPermissionDialog.value = false;
    return;
  }

  showGuide.value = true;

  Notification.requestPermission().then(async permission => {
    if (permission === "granted") {
      showTestNotification();


      const token = auth.user.access;
     
      if (token) {
        console.log("2:",token)

        await notification.subscribeUser(token);
      }
    }

    showPermissionDialog.value = false;
    showGuide.value = false;
  });
}

function showTestNotification() {
  new Notification("اعلان فعال شد!", {
    body: "شما اجازه دریافت اعلان‌ها را صادر کردید.",
    icon: "/img/ali.png"
  });
}

function dismiss() {
  showPermissionDialog.value = false;
}
</script>


<style scoped>
.overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(6px);
  z-index: 9998;
}

.permission-dialog {
  position: fixed;
  top: 50%; left: 50%;
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

.loading {
  margin-top: 20px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #4caf50;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
  margin-left: auto;
  margin-right: 0;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
