"use client";

import { Button } from "@/components/ui/button";
import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";

type Theme = "light" | "dark";

const useTheme = () => {
  const [theme, setTheme] = useState("dark");
  const getInitialTheme = (): Theme => {
    if (localStorage.theme === "light" || localStorage.theme === "dark") {
      return localStorage.theme;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  };

  useEffect(() => {
    const theme = getInitialTheme();
    window.document.documentElement.classList.add(theme);
    setTheme(theme);
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === "light" ? "dark" : "light";

    const rootEl = window.document.documentElement;
    rootEl.classList.remove(theme);
    rootEl.classList.add(newTheme);

    setTheme(newTheme);
    localStorage.setItem("theme", newTheme);
  };

  return { theme, toggleTheme };
};

export const ThemeToggle = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <Button onClick={() => toggleTheme()} variant="outline">
      {theme === "dark" ? <Moon /> : <Sun />}
    </Button>
  );
};
