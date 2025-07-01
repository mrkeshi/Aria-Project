import { defineStore } from "pinia";
import { saveOneSignalUserId } from "@/services/notifications";
import { useToast } from "vue-toastification";

const toast = useToast();

export const useNotificationStore = defineStore({
  id: "notification",

  state: () => ({
    oneSignalUserId: null,
    isSubscribed: false,
  }),

  actions: {
    async saveUserId(userId, token) {
      try {
        await saveOneSignalUserId(userId, token);
        this.oneSignalUserId = userId;
        this.isSubscribed = true;
        toast.success("شناسه پوش نوتیفیکیشن با موفقیت ذخیره شد.");
      } catch (error) {
        toast.error("خطا در ذخیره شناسه پوش نوتیفیکیشن.");
        console.error(error);
      }
    },

    setSubscriptionStatus(status) {
      this.isSubscribed = status;
    },

    clear() {
      this.oneSignalUserId = null;
      this.isSubscribed = false;
    },
  },
});