import axios from "@/utils/axios"

export const startSubscription = async (plan, token) => {
  console.log("start:",token)
  const response = await axios.post(
    "/subscription/start/",
    { plan },
    {
      headers: {
        Authorization: `JWT ${token}`,
      },
    }
  )
  return response.data
}
export const verifySubscription = async (authority, status, token,plan) => {
  console.log("veify:",token)

  const response = await axios.get(
    `/subscription/verify/?authority=${authority}&status=${status}&plan=${plan}`,
    {
      headers: {
        Authorization: `JWT ${token}`,
      },
    }
  )
  return response.data
}
export const getSubscriptionStatus = async (token) => {
  const response = await axios.get("/subscription/status/", {
    headers: {
      Authorization: `JWT ${token}`,
    },
  });
  return response.data;
};