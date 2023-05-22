import "./globals.css";
import Providers from "./providers";
import { Navbar } from "./navbar";

export const metadata = {
  title: "Dog App",
  description: "",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="h-screen w-screen bg-white dark:bg-black text-black dark:text-white">
        <Providers>
          <Navbar />
          {children}
        </Providers>
      </body>
    </html>
  );
}
