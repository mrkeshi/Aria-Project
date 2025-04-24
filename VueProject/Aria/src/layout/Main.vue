<template>
<div>
<Header></Header>

<div class="row flex  ">
<div id="content" class="content px-6 py-8 flex flex-col w-[calc(95%-320px)] max-lg:w-full mx-auto -z-0 relative">
<RouterView></RouterView>
</div>
<Aside></Aside>
</div>
</div>
</template>
<script setup>
import { RouterView } from 'vue-router';
import Header from '../layout/Header.vue'
import Aside from '../layout/Aside.vue'

</script>

<style>

</style>