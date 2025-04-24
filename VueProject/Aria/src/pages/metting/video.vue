<template>


</template>

<style>

</style>



<script setup>
import { ZegoUIKitPrebuilt } from '@zegocloud/zego-uikit-prebuilt';
import { onMounted,reactive } from 'vue';
import { useUserStore } from '@/stores/user';
import { useAuthStore } from '@/stores/auth';
import { useRoute } from 'vue-router';
const user=useUserStore()
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
const updateMyUser = () => {

    Object.assign(myuser, { ...user.user });
 
};

onMounted(async ()=>{
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
    const appID = 75030366;
    const serverSecret = "553c98be65bd6cec3fd18e5be4ec57d2";
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

</script>