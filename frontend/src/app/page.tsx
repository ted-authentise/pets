"use client";
import { Button } from "@/components/ui/button";
import { useQuery } from "@tanstack/react-query";

export default function Home() {
  const { data: dogImageUrl, refetch } = useQuery(["dog image"], {
    queryFn: async () => {
      const res = await (
        await fetch("https://dog.ceo/api/breeds/image/random")
      ).json();
      const url = (res as { message: string }).message;
      return url;
    },
  });
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <img src={dogImageUrl} width={100} height={100}></img>
      <Button onClick={() => void refetch()}>Next Dog</Button>
    </main>
  );
}
