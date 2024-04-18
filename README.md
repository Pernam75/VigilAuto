<p align="center">
  <a href="" rel="noopener">
 <img src="img/VigilAutobanner.png" alt="Project logo"></a>
</p>
<h3 align="center">Vigil'Auto</h3>

<div align="center">

<!-- [![Hackathon](https://img.shields.io/badge/hackathon-name-orange.svg)](http://hackathon.url.com) -->
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/julesrubin/VigilAuto.svg)](https://github.com/julesrubin/VigilAuto/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/julesrubin/VigilAuto.svg)](https://github.com/julesrubin/VigilAuto/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center">Revolutionize road safety with Vigil'Auto, our in-vehicle solution that analyzes driver behavior to predict driving under 
    the influence of alcohol, using machine learning and generative AI technologies to monitor the driver and provide real-time alerts.
    <br>
</p>

## 📝 Table of Contents

- [Vivatech 2024 Software République Challenge](#problem_statement)
- [Our Solution](#idea)
- [Future Scope](#future_scope)
- [Getting Started](#getting_started)
- [Built With](#tech_stack)
- [Authors](#authors)
- [License](#license)

## 🧐 Vivatech 2024 Software République Challenge <a name = "problem_statement"></a>

<!-- It is useful to design and follow a specific format when writing a problem statement. While there are several options
for doing this, the following is a simple and straightforward template often used in Business Analysis to maintain
focus on defining the problem.

- IDEAL: This section is used to describe the desired or “to be” state of the process or product. At large, this section
  should illustrate what the expected environment would look like once the solution is implemented.
- REALITY: This section is used to describe the current or “as is” state of the process or product.
- CONSEQUENCES: This section is used to describe the impacts on the business if the problem is not fixed or improved upon.
  This includes costs associated with loss of money, time, productivity, competitive advantage, and so forth.

Following this format will result in a workable document that can be used to understand the problem and elicit
requirements that will lead to a winning solution. -->

This project was developped as part of the Challenge Vivatech 2024 Software République Talent Academy. The goal of the challenge is to foster innovation in generative AI across various themes including health, well-being, electric vehicle experience, and road safety. The aim of the project is to protect vulnerable road users and enhance the human-vehicle relationship through the development of new products or services.

## 💡 Our Solution <a name = "idea"></a>

<!-- This section is used to describe potential solutions.

Once the ideal, reality, and consequences sections have been
completed, and understood, it becomes easier to provide a solution for solving the problem. -->

We propose Vigil'Auto, an in-vehicle solution that analyzes driver behavior using Computer Vision algorithms and predicts blood alcohol level of the driver. Then it provides a vocal conversational agent based on Mixtral 8x7B large language model to monitor the driver and provide real-time alerts. The agent is aimed to convince the driver to stop driving if the blood alcohol level is too high.

<!-- ## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

<!-- - What are the dependencies of your project?
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if
  appropriate, describe how these limitations could point to the need for further research. --> -->

## 🚀 Future Scope <a name = "future_scope"></a>

- The conversationnal agent could be improved by fine-tuning the Mixtral 8x7B model on a specific conversational dataset to make it more efficient.
- The computer vision classification model is trained on features extracted from training dataset, meaning that the inference process should extract the same features from the input image. This could be improved by using a model that can directly process the input image.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes. 
<!-- See [deployment](#deployment) for notes on how to deploy the project on a live system. -->

### Prerequisites

<!-- What things you need to install the software and how to install them.

```
Give examples
``` -->

- Python 3.10.14 or higher

- Install ffmpeg for audio processing

MacOS:
```bash
brew install ffmpeg
```

Ubuntu:
```bash
sudo apt-get install ffmpeg
```

Windows *(Not tested)*:
- Download the latest version of ffmpeg from [here](https://ffmpeg.org/download.html)
- Extract the zip file and add the bin folder to your PATH

- Go to [Groq Cloud Console](https://console.groq.com/playground) and create an account to get your API key. The free version will let you make 30 requests per minute with a maximum of 18,000 tokens per minute. We used Mixtral 8x7B model for our conversational agent but you can also use gemma-7B or Llama-70B models.

- Go to [ElevenLab Website](https://elevenlabs.io/) and create an account to get your API key. The free version will let you make 10k characters quota per month. You also need to chose a voice for the Text-to-Speech and add it to you voice library. We used the Nicolas' voice for our conversational agent (id: ```aQROLel5sQbj1vuIVi6B```) but you can provide your own voice id in the ```config/config.yaml``` file in the ```url``` field.

### Installing

<!-- A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
``` -->

1. Clone the repository

```bash
git clone https://github.com/julesrubin/VigilAuto.git
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Create a secret.yaml in the config folder and provide your Groq API key and ElevenLab API key
```yaml
llm:
  groq_api_key: "<YOUR_GROQ_API_KEY>"
tts:
  elevenlab_key: "<YOUR_ELEVENLAB_API_KEY>"
```

4. Run the application

```bash
python app.py
```

<!-- ## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system. -->

## ⛏️ Built With <a name = "tech_stack"></a>

<!-- - [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment -->

- [Python](https://www.python.org/) - Programming language
- [Whishper](https://openai.com/research/whisper) - Generative AI model for Speech-to-Text
- [Mixtral 8x7B](https://mistral.ai/fr/news/mixtral-of-experts/) - Large language model for conversational agent
- [Groq Cloud](https://console.groq.com/playground) - API for Mixtral 8x7B conversational agent

## ✍️ Authors <a name = "authors"></a>

- [@julesrubin](https://github.com/julesrubin) - LLM conversational agent and Speech-to-Text
- [@Luzartug](https://github.com/Luzartug) - Blood Alcohol Level prediction and Text-to-Speech
- [@Ayman](https://github.com/Senshiben-efrei)
- [@Dounia](https://github.com/)

See also the list of [contributors](https://github.com/julesrubin/VigilAuto/contributors)
who participated in this project.

<!-- ## 🎉 Acknowledgments <a name = "acknowledgments"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References -->

## 📜 License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
