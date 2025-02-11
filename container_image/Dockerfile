FROM ghcr.io/huggingface/text-generation-inference:latest
#https://github.com/huggingface/text-generation-inference/blob/main/Dockerfile

RUN conda install curl --yes

RUN pip install pythonping 
RUN pip install speedtest-cli 

COPY initial_check.py /initial_check.py
COPY imds_reallocate.py /imds_reallocate.py
COPY check_gpu.py /check_gpu.py
COPY check_network.py /check_network.py

COPY lt0_health_check.sh /lt0_health_check.sh
COPY lt1_inference_non_streaming.sh /lt1_inference_non_streaming.sh
COPY lt2_inference_streaming.sh /lt2_inference_streaming.sh
COPY lt3_network_check.sh /lt3_network_check.sh

RUN chmod +x /lt0_health_check.sh
RUN chmod +x /lt3_network_check.sh
RUN chmod +x /lt1_inference_non_streaming.sh
RUN chmod +x /lt2_inference_streaming.sh

COPY ./salad-tgi-entrypoint.sh /salad-tgi-entrypoint.sh
RUN chmod +x /salad-tgi-entrypoint.sh

ENTRYPOINT ["/salad-tgi-entrypoint.sh"]

