import { defineStore } from "pinia";
import { useToast } from "vue-toastification";
import { startSubscription, verifySubscription, getSubscriptionStatus } from "@/services/Sub";

let paymentToastTimeout = null;

export const useSubStore = defineStore({
  id: "Sub",
  state: () => ({
    Getlevel: 0,
    level: 1,
    Permissions: {
      addtask: false,
      adduser: false,
      addprject: false,
      support: false,
      video: false,
      notification: false,
      issuese: false,
    },
    countDetail: {
      task: 0,
      user: 0,
      project: 0,
    },
    limits: {},
    manager_plan: "free",
    manager_plan_active: false,
    isub: true, 
    loading: false,
    error: null,
    refId: null,
    success: false,
    startedAt: null,
    expiresAt: null,
    isActive: false,
    remainingDays: 0,
    paymentToastShown: false,
  }),

  actions: {
    async addSub(token, plan = "silver") {
      const toast = useToast();
      this.paymentToastShown = false;
      if (this.Getlevel === 3) plan = "gold";
      try {
        const data = await startSubscription(plan, token);
        if (data.url) {
          window.location.href = data.url;
        } else {
          toast.error("خطا در دریافت لینک پرداخت");
        }
      } catch (error) {
        console.error("خطای خرید اشتراک:", error);
        toast.error("خرید اشتراک با خطا مواجه شد");
      }
    },

    async verifyPayment(authority, status, token, pane) {
      const toast = useToast();
      if (this.paymentToastShown) return;
      this.loading = true;
      this.error = null;
      this.success = false;
      this.refId = null;
      try {
        const result = await verifySubscription(authority, status, token, pane);
        this.refId = result.ref_id;
        this.success = true;
        this.paymentToastShown = true;
        return result;
      } catch (err) {
        this.error = err.response?.data?.detail || "خطا در تأیید پرداخت رخ داد.";
        toast.error(this.error);
        throw err;
      } finally {
        this.loading = false;
      }
    },

    async fetchSubscriptionStatus(token) {
      const toast = useToast();
      this.loading = true;
      this.error = null;
      try {
        const data = await getSubscriptionStatus(token);

        this.Getlevel = ["free", "silver", "gold"].indexOf(data.plan);
        this.countDetail.project = data.total_projects;
        this.countDetail.task = data.total_tasks;
        this.countDetail.user = data.total_users;
        this.limits = data.limits;

        this.startedAt = data.started_at;
        this.expiresAt = data.expires_at;
        this.isActive = data.is_active;
        this.remainingDays = data.remaining_days;
        this.manager_plan = data.manager_plan;
        this.manager_plan_active = data.manager_plan_active;
        this.isub = data.isub; 

        this.level = this.Getlevel + 1;

        const { max_projects, max_tasks_per_project, max_users_per_project } = data.limits;
        const { project, task, user } = this.countDetail;
        const isUnderProjectLimit = max_projects === null || project < max_projects;
        const isUnderTaskLimit = max_tasks_per_project === null || task < max_tasks_per_project;
        const isUnderUserLimit = max_users_per_project === null || user < max_users_per_project;

        const isGold = data.plan === "gold";
        const isSilver = data.plan === "silver";
        const isFree = data.plan === "free";
        const isProjectCountZero = project === 0;

        this.Permissions = {
          addtask: isGold || isUnderTaskLimit,
          adduser: isGold || isUnderUserLimit,
          addprject: isGold || isUnderProjectLimit || isProjectCountZero,
          support: isGold || isSilver,
          video: isGold,
          notification: isGold || isSilver,
          issuese: isGold || isSilver,
        };
      } catch (err) {
        this.error = "خطا در دریافت اطلاعات اشتراک";
      } finally {
        this.loading = false;
      }
    },
  },
});



