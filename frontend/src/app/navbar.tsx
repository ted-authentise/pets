import { ThemeToggle } from "./theme-toggle";

export const Navbar = () => {
  return (
    <nav className="fixed top-0 w-screen h-16 flex flex-row justify-between items-center px-4">
      <h1 className="font-semibold text-lg">Dogs</h1>

      <ThemeToggle />
    </nav>
  );
};
