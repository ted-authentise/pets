"use client";
import { Button } from "@/components/ui/button";
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";
import { BreedPicker } from "./breed-picker";

export default function Home() {
  const [breed, setBreed] = useState("");
  const { data: dogImageUrl, refetch } = useQuery(["dog image", breed], {
    queryFn: async () => {
      const res = await (
        await fetch(
          breed === ""
            ? "https://dog.ceo/api/breeds/image/random"
            : `https://dog.ceo/api/breed/${breed}images/random`
        )
      ).json();
      const url = (res as { message: string }).message;
      return url;
    },
  });
  return (
    <main className="flex min-h-screen flex-col items-center justify-center pt-16 gap-4">
      <BreedPicker value={breed} setValue={setBreed} />
      <img
        src={dogImageUrl}
        className="w-[50vh] h-[50vh] object-contain rounded"
        alt="Dog image"
      />
      <Button onClick={() => void refetch()}>Next Dog</Button>
    </main>
  );
}
