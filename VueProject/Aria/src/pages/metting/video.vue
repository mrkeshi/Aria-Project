<template>


</template>

<style>

</style>



<script setup>
import "@/assets/newstyle.css"
import { ZegoUIKitPrebuilt } from '@zegocloud/zego-uikit-prebuilt';
import { onMounted,reactive } from 'vue';
import { useUserStore } from '@/stores/user';
import { useAuthStore } from '@/stores/auth';
import { useRoute ,useRouter} from 'vue-router';
import { useSubStore } from "@/stores/SubStore";
import { useToast } from "vue-toastification";
const user=useUserStore()
const subStore=useSubStore()
const auth=useAuthStore()
const myuser=reactive({
             avatar: null,
            id: null,
            email: null,
            current_project:null,
            firstname:null,
            lastname:null,
            level:null,
            rollname:''
})
const route=useRoute()
const router=useRouter()
const updateMyUser = () => {

    Object.assign(myuser, { ...user.user });
 
};
const toast=useToast()
onMounted(async ()=>{
    await subStore.fetchSubscriptionStatus(auth.user.access);
    if((!subStore.isActive || subStore.level<3) && (subStore.manager_plan!="gold" || !subStore.manager_plan_active)){
      router.push({'name':'dashbaord'})
      toast.info("قابلیت کنفرانس ویدئویی توسط مدیر پروژه فعال نشده است.")
    }
    await auth.verifyAction(route.path)

       await user.getDetail()
       await user.getLeveAction(user.user.id)
   
    await updateMyUser();
    console.log(myuser);
    function getUrlParams(url) {
        let urlStr = url.split('?')[1];
        const urlSearchParams = new URLSearchParams(urlStr);
        const result = Object.fromEntries(urlSearchParams.entries());
        return result;
    }


        // Generate a Token by calling a method.
        // @param 1: appID
        // @param 2: serverSecret
        // @param 3: Room ID
        // @param 4: User ID
        // @param 5: Username
    const roomID = getUrlParams(window.location.href)['roomID'] || (Math.floor(Math.random() * 10000) + "");
    const userID = Math.floor(Math.random() * 10000) + "";
    const userName = user.user.firstname ? user.user.firstname+" "+user.user.lastname : user.user.email;
    const appID = 1707325129;
    const serverSecret = "6a2288e8fe7a906eaf6383b23d702b5b";
    const kitToken = ZegoUIKitPrebuilt.generateKitTokenForTest(appID, serverSecret, roomID, userID, userName);

    
        const zp = ZegoUIKitPrebuilt.create(kitToken);
        zp.joinRoom({
            container: document.querySelector("#root"),
            sharedLinks: [{
                name: 'Personal link',
                url: window.location.protocol + '//' + window.location.host  + window.location.pathname + '?roomID=' + roomID,
            }],
            scenario: {
                mode: ZegoUIKitPrebuilt.VideoConference,
            },
                
           	turnOnMicrophoneWhenJoining: true,
           	turnOnCameraWhenJoining: true,
           	showMyCameraToggleButton: true,
           	showMyMicrophoneToggleButton: true,
           	showAudioVideoSettingsButton: true,
           	showScreenSharingButton: true,
           	showTextChat: true,
           	showUserList: true,
           	maxUsers: 50,
           	layout: "Grid",
           	showLayoutButton: true,
         
            });
})
window.onload = function () {

   
}
document.addEventListener("DOMContentLoaded", () => {
  const style = document.createElement('style');
  style.textContent = `
    @media (max-width: 768px) {
      #zego-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding: 1rem;
        box-sizing: border-box;
        overflow: hidden !important;
      }

      #zego-container video {
        width: 100% !important;
        height: auto !important;
        max-height: 40vh;
        object-fit: contain;
        margin-bottom: 1rem;
      }

      #zego-container .rQfcdxdAd98I2u3wR_Xv {
        width: 100% !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
      }

      #zego-container input {
        width: 90% !important;
        max-width: 300px;
      }

      #zego-container button {
        width: auto;
      }
    }
  `;
  document.head.appendChild(style);
});
</script>

<style>


</style>
