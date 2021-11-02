<p align="center"><img width="700" src="./media/logo/Transcriptor.png"></p>

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![GitHub issues](https://img.shields.io/github/issues-raw/secheaper/transcriptor)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/secheaper/transcriptor)
![Github pull requests](https://img.shields.io/github/issues-pr/secheaper/transcriptor)
[![GitHub forks](https://img.shields.io/github/forks/secheaper/transcriptor)](https://github.com/secheaper/transcriptor/network)
[![DOI](https://zenodo.org/badge/409326011.svg)](https://zenodo.org/badge/latestdoi/409326011)
[![GitHub license](https://img.shields.io/github/license/anshulp2912/scrivener)](https://github.com/anshulp2912/scrivener/blob/main/LICENSE)
![Lines of code](https://img.shields.io/badge/Lines%20of%20Code-1K-blue)
![Coverage](https://img.shields.io/badge/Coverage-97%25-red)
![Contributors](https://img.shields.io/badge/Contributors-5-yellowgreen)

Transcriptor is a web application that generates a quick summary and analyzes sentiment for videos using advanced Natural Language Processing techniques. 
- **Fast**: Transcriptor helps you save over 70% of your time by quickly providing a summary to highlight key points from videos
- **Easy**: A simple and friendly web interface is provided used to summarize videos 
- **Powerful**: Transcriptor uses TensorFlow libraries to get highly accurate summaries in no time

<p align="center">
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#sunflower-demo-website">Demo Website</a>
  ::
  <a href="#thought_balloon-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>	
   ::
  <a href="#heart-acknowledgements">Acknowledgements</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
    ::
  <a href="#email-support">Support</a>
</p>

:rocket: Installation
---
1. Clone the Git repository and `cd` into the new repo
```
git clone https://github.com/secheaper/transcriptor.git
cd slash
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those
```
pip3 install -r requirements.txt
```
3. Once all the requirements are installed, you will have to ```cd``` into the ```source``` folder. Once in the ```source``` folder, use the streamlit command to run the ```transcriptor.py``` file
```
cd source
streamlit transcriptor.py
```
4. If all went well, you should see the Network URL where this application is running on your local computer

:sunflower: Demo Webiste
---
The project is deployed on Streamlit Cloud
- [Streamlit](https://share.streamlit.io/secheaper/transcriptor/main/source/transcriptor.py)

## License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/anshulp2912/scrivener/blob/main/LICENSE) for more details.

## Contributions <a name="Contributions"></a>
Please see our [CONTRIBUTING.md](https://github.com/anshulp2912/scrivener/blob/main/CONTRIBUTING.md) for instructions on how to contribute to the project by completing some of the issues.

## Future Scope <a name="FutureScope"></a>
For enhancement of this project following functionalities can be implemented
- Currently our application supports youtube videos and videos with .mp4 extension. Provide support for other video formats
- Perform summarization for videos in languages other than English
- Generate summary of Podcasts or other audiofiles
- Provide summary in form of video
- Generate summary of videos for specific time frames
- Compare various Summarization models and provide optimal summary
- UI Enhancement
- Provide summary in form of audio
- Generate summary of audio for specific time frames
- Adding Chrome extension for SCRIVENER
- Provide Sentiment Analysis of the generated summary
- Develop a Discord BOT for SCRIVENER

:heart: Acknowledgements
---
We would like to thank Dr. Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project. Also thanks to the amazing teams at [Streamlit](https://streamlit.io/), [Huggingface](https://huggingface.co/) and [Shields.io](https://shields.io/) for their amazing projects!

:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="http://www.shubhammankar.com/"><img src="https://avatars.githubusercontent.com/u/29366125?v=4" width="75px;" alt=""/><br /><sub><b>Shubham Mankar</b></sub></a></td>
    <td align="center"><a href="https://github.com/pratikdevnani"><img src="https://avatars.githubusercontent.com/u/43350493?v=4" width="75px;" alt=""/><br /><sub><b>Pratik Devnani</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/moksh98"><img src="https://avatars.githubusercontent.com/u/29693765?v=4" width="75px;" alt=""/><br /><sub><b>Moksh Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://rahilsarvaiya.tech/"><img src="https://avatars0.githubusercontent.com/u/32304956?v=4" width="75px;" alt=""/><br /><sub><b>Rahil Sarvaiya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/annie0467"><img src="https://avatars.githubusercontent.com/u/17164255?v=4" width="75px;" alt=""/><br /><sub><b>Anushi Keswani</b></sub></a><br /></td>
  </tr>
</table>

:email: Support
---

For any queries and help, please reach out to us at: secheaper@gmail.com
