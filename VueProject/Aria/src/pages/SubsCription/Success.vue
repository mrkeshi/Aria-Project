<template>
  <div class="w-full min-h-screen bg-gray-50 flex items-center justify-center px-4 py-20">
    <div class="bg-white max-w-md w-full shadow-lg rounded-xl p-8 border text-center space-y-6">

      <div v-if="success" class="mx-auto w-16 h-16 flex items-center justify-center bg-green-100 rounded-full text-green-600">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path d="M5 13l4 4L19 7" />
        </svg>
      </div>

      <div v-else-if="error" class="mx-auto w-16 h-16 flex items-center justify-center bg-red-100 rounded-full text-red-600">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path d="M6 18L18 6M6 6l12 12" />
        </svg>
      </div>

      <h2 class="text-2xl font-bold text-gray-800">
        {{ success ? "خرید با موفقیت انجام شد" : error ? "پرداخت ناموفق بود" : "در حال بررسی پرداخت..." }}
      </h2>

      <p class="text-sm text-gray-500">
        {{ success ? "اشتراک شما با موفقیت فعال شد." : errorMessage || "لطفاً منتظر بمانید..." }}
      </p>

      <div v-if="refId" class="bg-gray-100 text-gray-800 font-mono text-sm rounded-md px-4 py-3">
        کد رهگیری: <span class="font-bold">{{ refId }}</span>
      </div>

      <div class="pt-4" v-if="!loading">
        <a href="/dashboard" class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md transition-all">
          بازگشت به داشبورد
        </a>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toastification'

import { useUserStore } from '@/stores/user'
import { useSubStore } from '@/stores/SubStore'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const toast = useToast()
const userStore = useAuthStore()
const subStore = useSubStore()

const success = ref(false)
const error = ref(false)
const errorMessage = ref("")
const refId = ref(null)
const loading = ref(true)

onMounted(async () => {
  const authority = route.query.Authority
  const statusParam = route.query.Status

  if (!authority || !statusParam || statusParam !== 'OK') {
    error.value = true
    errorMessage.value = "پرداخت توسط کاربر لغو شد یا اطلاعات ناقص است."
    loading.value = false
    return
  }

  try {
    const result = await subStore.verifyPayment(authority, statusParam, userStore.user.access,route.query.plan)
    refId.value = result.ref_id
    success.value = true
    toast.success("پرداخت با موفقیت تأیید شد.")
  } catch (err) {
    error.value = true
    errorMessage.value = subStore.error
  } finally {
    loading.value = false
  }
})
</script>
