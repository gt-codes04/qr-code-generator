# Reflection – Dockerizing the QR Code Generator Application

This was my first time fully containerizing a Python app with Docker. The idea was to take an initial simple QR Code Generator script and turn it into a portable, secure, and reproducible Docker image that can be run anywhere.

I had some issues initially with the Dockerfile configuration and wrapping my head around how the layers were working. I had a couple of issues where the output file wasn't being generated due to the fact that the filename didn't have an adequate image extension. Fixing that by adding \".png\" to the output path was something I learned about how small things can ruin an/containerized process. I also learned how to mount individual directories on my host machine with Docker volumes so that the generated QR codes actually end up being stored on my host machine.

Security and performance were key considerations. I used `python:3.12-slim-bullseye` as a base, made it light, installed using `--no-cache-dir` to reduce image size, and executed as a non-root user inside the container. All these made the container secure and production-ready.

After developing and testing locally, I pushed the image to my Docker Hub account (`gunateja04/qr-code-generator-app`) and set up a GitHub Actions workflow to automatically build and push the image whenever I push to the main branch. Seeing that automated pipeline run successfully was a highlight—it gave the project a sense of done-ness.

Overall, this exercise helped me connect the dots between so many of these ideas: Python packaging, Docker building, and CI/CD automation. This was actually a real-world example of how actual applications are deployed to cloud environments.
