import { defineStore } from "pinia";
import { savePushSubscription } from "@/services/notifications";
import { useToast } from "vue-toastification";

const toast = useToast();

export const useNotificationStore = defineStore({
  id: "notification",

  state: () => ({
    isSubscribed: false,
    subscriptionInfo: null,
  }),

  actions: {
    async subscribeUser(token) {
      try {
     
        const registration = await navigator.serviceWorker.ready;

        const existingSubscription = await registration.pushManager.getSubscription();

        let subscription = existingSubscription;
        if (!subscription) {
          const vapidPublicKey ="BI6n1krZ0FQZBJLz-N7jaCfffuaH6s0s8dGOpMwaOCeqtWdlIoUGep7QoEVX2C938j1PjMEZuNQtcJwSlXl6J3E";
          const convertedVapidKey = this._urlBase64ToUint8Array(vapidPublicKey);

          subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: convertedVapidKey,
          });
        }

        const subscriptionData = subscription.toJSON();

        await savePushSubscription(subscriptionData, token);
        this.subscriptionInfo = subscriptionData;
        this.isSubscribed = true;

        toast.success("اشتراک پوش با موفقیت ذخیره شد.");
      } catch (error) {
        console.error("Push subscription error:", error);
        toast.error("خطا در ذخیره اشتراک پوش.");
      }
    },

    clear() {
      this.isSubscribed = false;
      this.subscriptionInfo = null;
    },

    _urlBase64ToUint8Array(base64String) {
      const padding = "=".repeat((4 - base64String.length % 4) % 4);
      const base64 = (base64String + padding).replace(/\-/g, "+").replace(/_/g, "/");
      const rawData = atob(base64);
      const outputArray = new Uint8Array(rawData.length);
      for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
      }
      return outputArray;
    },
  },
});
