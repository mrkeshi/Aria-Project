<template>
  <div class="w-full min-h-screen bg-gray-50 flex items-center justify-center px-4 py-20">
    <div class="bg-white max-w-md w-full shadow-lg rounded-xl p-8 border text-center space-y-6">
      <div class="mx-auto w-16 h-16 flex items-center justify-center bg-blue-100 rounded-full text-blue-600">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2"
          viewBox="0 0 24 24">
          <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      </div>

      <h2 class="text-2xl font-bold text-gray-800">تایید خرید اشتراک</h2>
      <p class="text-sm text-gray-500">
        آیا مطمئن هستید که می‌خواهید اشتراک را خریداری کنید؟ این عملیات قابل بازگشت نیست.
      </p>

      <div class="flex flex-col sm:flex-row gap-3 justify-center">
        <button
          @click="confirmPurchase"
          class="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md transition-all"
        >
          تایید خرید
        </button>
        <router-link
          to="/dashboard"
          class="w-full sm:w-auto bg-gray-100 hover:bg-gray-200 text-gray-700 px-6 py-2 rounded-md transition-all text-center"
        >
          انصراف
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'
import { useSubStore } from '@/stores/SubStore'

const subStore = useSubStore()
const authStore = useAuthStore()
const route = useRoute()
const toast = useToast()

const plan = route.query.plan || 'silver'

const confirmPurchase = async () => {
  const token = authStore.user.access
  if (!token) {
    toast.error('برای خرید اشتراک ابتدا وارد شوید')
    return
  }

  toast.info('در حال هدایت به درگاه پرداخت...')
  try {
    await subStore.addSub(token, plan)
    toast.success('در حال اتصال به درگاه...')
  } catch (error) {
    toast.error('خطا در شروع فرآیند خرید')
  }
}
</script>
