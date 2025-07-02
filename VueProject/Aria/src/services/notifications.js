import axios from "@/utils/axios";

export const savePushSubscription = async (subscriptionInfo, token) => {
  const response = await axios.post(
    "noti/push/save/",
    { subscription_info: subscriptionInfo },
    {
      headers: {
        Authorization: `JWT ${token}`,
      },
    }
  );
  return response.data;
};
