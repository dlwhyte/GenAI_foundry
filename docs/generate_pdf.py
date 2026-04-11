#!/usr/bin/env python3
"""
Generate Student_Quick_Start.pdf for GenAI Foundry
Run from repo root: python docs/generate_pdf.py
Requires: pip install reportlab
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_CENTER, TA_LEFT


NAVY   = colors.HexColor('#1B2A4A')
ORANGE = colors.HexColor('#F5A623')
LGREY  = colors.HexColor('#F5F5F5')
MGREY  = colors.HexColor('#CCCCCC')
WHITE  = colors.white
GREEN  = colors.HexColor('#2E7D32')

def s(name, **kw):
    return ParagraphStyle(name, **kw)

BASE  = s('Base', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.black)
BOLD  = s('Bd',   fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.black)
HDRW  = s('Hw',   fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=WHITE)
TITLE = s('Ti',   fontName='Helvetica-Bold', fontSize=22, leading=28, textColor=WHITE, alignment=TA_CENTER)
SUB   = s('Su',   fontName='Helvetica', fontSize=13, leading=18, textColor=ORANGE, alignment=TA_CENTER)
H2    = s('H2',   fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=NAVY)
H3    = s('H3',   fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=NAVY)
BODY  = s('Bo',   fontName='Helvetica', fontSize=9, leading=13, textColor=colors.black)
CODE  = s('Co',   fontName='Courier', fontSize=8, leading=11, textColor=colors.black, backColor=LGREY)
WARN  = s('Wa',   fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.HexColor('#B71C1C'))
NOTE  = s('No',   fontName='Helvetica-Oblique', fontSize=8, leading=11, textColor=colors.HexColor('#555555'))

def p(text, style=BASE): return Paragraph(text, style)
def h(text):             return Paragraph(text, HDRW)
def sp(n=6):             return Spacer(1, n)
def hr():                return HRFlowable(width='100%', thickness=1, color=MGREY, spaceAfter=4)

NAV_STYLE = TableStyle([
    ('BACKGROUND',  (0,0), (-1,0),  NAVY),
    ('TEXTCOLOR',   (0,0), (-1,0),  WHITE),
    ('FONTNAME',    (0,0), (-1,0),  'Helvetica-Bold'),
    ('FONTSIZE',    (0,0), (-1,-1), 8),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, LGREY]),
    ('GRID',        (0,0), (-1,-1), 0.3, MGREY),
    ('TOPPADDING',  (0,0), (-1,-1), 4),
    ('BOTTOMPADDING',(0,0),(-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING',(0,0), (-1,-1), 6),
    ('VALIGN',      (0,0), (-1,-1), 'TOP'),
])


def tbl(data, col_widths, style=NAV_STYLE):
    t = Table(data, colWidths=col_widths)
    t.setStyle(style)
    return t


def cover_page(W, M):
    elems = []
    # Hero banner
    banner_data = [[p('GenAI Foundry', TITLE)]]
    banner = Table(banner_data, colWidths=[W - 2*M])
    banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('TOPPADDING', (0,0), (-1,-1), 22),
        ('BOTTOMPADDING', (0,0), (-1,-1), 22),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    elems.append(banner)
    elems.append(sp(8))
    elems.append(p('Quick Start Guide — Applied Generative AI', SUB))
    elems.append(sp(4))
    elems.append(p('Notebooks + Interactive Streamlit Demos', NOTE))
    elems.append(sp(14))
    elems.append(hr())
    elems.append(sp(10))

    elems.append(p('What is GenAI Foundry?', H2))
    elems.append(sp(4))
    elems.append(p('GenAI Foundry is a hands-on learning series that takes you from the basics of how Large Language Models work all the way to building RAG (Retrieval-Augmented Generation) pipelines and interactive AI demos. Everything runs in Google Colab or Docker — no local Python setup required.', BODY))
    elems.append(sp(12))

    # Learning path table
    elems.append(p('Learning Path Overview', H2))
    elems.append(sp(6))
    path_data = [
        [h('#'), h('Notebook'), h('Topic'), h('API Key?')],
        [p('1'), p('Tokens and Embeddings'), p('How LLMs break text into tokens and represent meaning'), p('Free')],
        [p('2'), p('Semantic Similarity'), p('How embeddings capture meaning and measure similarity'), p('Free')],
        [p('3'), p('Search with Embeddings'), p('Keyword vs. semantic search, chunking, and RAG foundations'), p('Free')],
        [p('4'), p('Model Selection & Tradeoffs'), p('Capability, speed, cost, and context window tradeoffs'), p('Free')],
        [p('5'), p('Simple Chatbot'), p('Build your first LLM-powered chatbot with OpenAI'), p('Required')],
        [p('6'), p('Temperature & Tokens'), p('See how temperature and max_tokens change LLM output'), p('Required')],
        [p('7'), p('Prompt Engineering'), p('Zero-shot prompting, system messages, output formatting'), p('Required')],
        [p('8'), p('Few-Shot / Zero-Shot'), p('Teaching the model with examples vs. instructions alone'), p('Required')],
        [p('9'), p('Simple RAG Application'), p('End-to-end Retrieval-Augmented Generation pipeline'), p('Required')],
        [p('10'), p('LangChain Basics'), p('Chains, prompts, and memory with LangChain'), p('Required')],
        [p('11'), p('Fine-Tuning Basics'), p('Introduction to fine-tuning foundation models'), p('Required')],
        [p('12'), p('What is an Agent?'), p('From chatbots to agents — the Observe-Think-Act loop'), p('Free')],
    ]
    elems.append(tbl(path_data, [0.3*inch, 1.5*inch, 3.2*inch, 1.0*inch]))
    elems.append(sp(10))

    # Interactive demos
    elems.append(p('Interactive Streamlit Demos', H2))
    elems.append(sp(6))
    demo_data = [
        [h('Demo'), h('Description'), h('API Key?')],
        [p('RAG Visual Explorer'), p('See chunking, embeddings, and vector search in action — no coding required'), p('Free')],
        [p('Ontology & Counterfactual'), p('Knowledge graphs and what-if analysis; LLM validation of AI outputs'), p('Required')],
        [p('RAG Chat with Estel'), p('Upload your own PDF or TXT and chat with it using full RAG pipeline'), p('Required')],
        [p('Prompt Injection Defense'), p('Explore AI guardrails and how prompt injection attacks work'), p('Required')],
    ]
    elems.append(tbl(demo_data, [1.5*inch, 3.5*inch, 1.0*inch]))
    return elems


def setup_page(W, M):
    elems = []
    elems.append(p('Getting Started — Docker Setup', H2))
    elems.append(sp(4))
    elems.append(p('The interactive demos run as a multi-page Streamlit app inside a single Docker container. Follow these steps:', BODY))
    elems.append(sp(8))

    # Docker steps
    docker_data = [
        [h('Step'), h('Command / Action')],
        [p('1. Clone the repo'),  p('git clone https://github.com/dlwhyte/GenAI_foundry.git')],
        [p('2. Enter the folder'), p('cd GenAI_foundry')],
        [p('3. Build the image'),  p('docker build -t genai-foundry .')],
        [p('4. Run the container'), p('docker run -p 8501:8501 genai-foundry')],
        [p('5. Open your browser'), p('http://localhost:8501')],
    ]
    elems.append(tbl(docker_data, [1.7*inch, 4.3*inch]))
    elems.append(sp(6))
    elems.append(p('<b>With an OpenAI API key</b> (required for Ontology demo and RAG Chat):', BODY))
    elems.append(sp(3))
    elems.append(p('docker run -p 8501:8501 -e OPENAI_API_KEY=sk-your-key-here genai-foundry', CODE))
    elems.append(sp(3))
    elems.append(p('Tip: Without the -e flag you can still enter your API key in the sidebar on any page that requires it.', NOTE))
    elems.append(sp(10))

    elems.append(p('Prerequisites', H3))
    elems.append(sp(4))
    prereq_data = [
        [h('Requirement'), h('Notes')],
        [p('Docker Desktop'), p('Download from docker.com/products/docker-desktop — free for personal use')],
        [p('Git'), p('Usually pre-installed on Mac/Linux; download from git-scm.com for Windows')],
        [p('OpenAI API Key'), p('Required for Part 2 notebooks and demos that call the OpenAI API')],
        [p('Google Account'), p('To open notebooks in Google Colab (free, no local setup)')],
    ]
    elems.append(tbl(prereq_data, [1.7*inch, 4.3*inch]))
    elems.append(sp(10))

    # Docker troubleshooting
    elems.append(p('Docker Troubleshooting', H3))
    elems.append(sp(4))
    trouble_data = [
        [h('Problem'), h('Fix')],
        [p('Port 8501 already in use'), p('Stop other Streamlit apps or use: docker run -p 8502:8501 genai-foundry')],
        [p('Docker daemon not running'), p('Open Docker Desktop and wait for the whale icon to appear in the menu bar')],
        [p('Build takes too long'), p('Normal on first run — Docker downloads ~1 GB of layers. Subsequent builds are cached')],
        [p('Container exits immediately'), p('Run: docker logs $(docker ps -lq) to see the error output')],
        [p('API key not working'), p('Check for spaces or newlines — key should start with sk- and have no extra characters')],
    ]
    elems.append(tbl(trouble_data, [2.0*inch, 4.0*inch]))
    return elems


def notebooks_page(W, M):
    elems = []
    elems.append(p('Running Notebooks in Google Colab', H2))
    elems.append(sp(4))
    elems.append(p('All notebooks open directly in Google Colab with a single click — no local Python install needed. Just click the Colab badge in the README.', BODY))
    elems.append(sp(8))

    elems.append(p('Part 1 — LLM Mechanics (No API Key Required)', H3))
    elems.append(sp(4))
    part1_data = [
        [h('#'), h('Notebook'), h('What You Will Learn')],
        [p('1'), p('Tokens and Embeddings'),     p('How LLMs tokenize text and represent meaning as number vectors')],
        [p('2'), p('Semantic Similarity'),       p('Cosine similarity, dot products, and how embeddings cluster meaning')],
        [p('3'), p('Search with Embeddings'),    p('Chunking, FAISS vector search, and RAG foundations step by step')],
        [p('4'), p('Model Selection & Tradeoffs'), p('GPT-4o vs GPT-4o-mini vs o1: speed, cost, context, and capability')],
    ]
    elems.append(tbl(part1_data, [0.3*inch, 1.8*inch, 3.9*inch]))
    elems.append(sp(8))

    elems.append(p('Part 2 — Introductory Concepts (OpenAI API Key Required)', H3))
    elems.append(sp(4))
    part2_data = [
        [h('#'), h('Notebook'), h('What You Will Learn'), h('Time')],
        [p('5'),  p('Simple Chatbot'),           p('Build your first chatbot with system messages and conversation history'), p('~15 min')],
        [p('6'),  p('Temperature & Tokens'),     p('Experiment with creativity vs. determinism and output length limits'), p('~20 min')],
        [p('7'),  p('Prompt Engineering'),       p('Zero-shot prompting, formatting, and system message design patterns'), p('~25 min')],
        [p('8'),  p('Few-Shot / Zero-Shot'),     p('Teaching the model by example vs. pure instruction'), p('~20 min')],
        [p('9'),  p('Simple RAG Application'),  p('Full RAG pipeline: embed your docs, search, and answer questions'), p('~30 min')],
        [p('10'), p('LangChain Basics'),         p('Chains, prompt templates, and memory using the LangChain framework'), p('~25 min')],
        [p('11'), p('Fine-Tuning Basics'),       p('Prepare datasets and fine-tune foundation models on custom data'), p('~30 min')],
    ]
    elems.append(tbl(part2_data, [0.4*inch, 1.6*inch, 3.1*inch, 0.9*inch]))
    elems.append(sp(8))

    elems.append(p('Part 3 — Bridge to Agentic AI (Free)', H3))
    elems.append(sp(4))
    part3_data = [
        [h('#'), h('Notebook'), h('What You Will Learn'), h('Time')],
        [p('12'), p('What is an Agent?'), p('The Observe-Think-Act loop: how agents differ from chatbots and RAG'), p('~20 min')],
    ]
    elems.append(tbl(part3_data, [0.4*inch, 1.6*inch, 3.1*inch, 0.9*inch]))
    elems.append(sp(8))
    elems.append(p('Getting an OpenAI API Key', H3))
    elems.append(sp(4))
    api_data = [
        [h('Step'), h('Action')],
        [p('1'), p('Go to: platform.openai.com')],
        [p('2'), p('Sign up or log in with a Google or email account')],
        [p('3'), p('Go to API Keys section and click Create new secret key')],
        [p('4'), p('Copy the key immediately — it is only shown once')],
        [p('5'), p('Add a small credit balance (a few dollars covers many sessions)')],
    ]
    elems.append(tbl(api_data, [0.4*inch, 5.6*inch]))
    elems.append(sp(4))
    elems.append(p('Cost note: Each notebook session typically costs pennies. RAG Chat and Ontology demos use more tokens but stay well under $0.10 per session with GPT-4o-mini.', NOTE))
    return elems


def demos_page(W, M):
    elems = []
    elems.append(p('Interactive Demo Guide', H2))
    elems.append(sp(4))
    elems.append(p('Once Docker is running (http://localhost:8501) you will see four demos in the sidebar. Here is what each one does and which notebooks it connects to.', BODY))
    elems.append(sp(10))

    # Demo 1
    elems.append(p('RAG Visual Explorer', H3))
    elems.append(sp(3))
    elems.append(p('Connects to: Notebooks 1, 2, 3, 9 — No API key required', NOTE))
    elems.append(sp(3))
    rag_data = [
        [h('Feature'), h('What It Shows')],
        [p('Chunking'),        p('Watch a document split into overlapping, searchable pieces')],
        [p('Embeddings'),      p('See text transform into numerical vectors in real time')],
        [p('Vector Space'),    p('Visualise how similar content clusters together in 2D/3D')],
        [p('Semantic Search'), p('Compare keyword search vs. meaning-based vector search side by side')],
    ]
    elems.append(tbl(rag_data, [1.5*inch, 4.5*inch]))
    elems.append(sp(10))

    # Demo 2
    elems.append(p('Ontology & Counterfactual Reasoning', H3))
    elems.append(sp(3))
    elems.append(p('Connects to: Notebooks 7, 8 — OpenAI API key required', NOTE))
    elems.append(sp(3))
    ont_data = [
        [h('Feature'), h('What It Shows')],
        [p('Ontology Explorer'),       p('Interactive knowledge graph of cybersecurity risks and relationships')],
        [p('Counterfactual Analysis'), p('Test what happens to risk scores when controls fail or are added')],
        [p('LLM Validation'),          p('Verify AI outputs against structured ground truth data')],
    ]
    elems.append(tbl(ont_data, [1.8*inch, 4.2*inch]))
    elems.append(sp(10))

    # Demo 3
    elems.append(p('RAG Chat with Estel', H3))
    elems.append(sp(3))
    elems.append(p('Connects to: Notebooks 9, 10 — OpenAI API key required', NOTE))
    elems.append(sp(3))
    chat_data = [
        [h('Step'), h('What To Do')],
        [p('1. Upload'),  p('Drag and drop any PDF or TXT file — your uploaded document becomes the knowledge base')],
        [p('2. Index'),   p('The app chunks, embeds, and stores your document in a FAISS vector database')],
        [p('3. Chat'),    p('Ask questions in plain English — answers are grounded in your document')],
        [p('4. Learn'),   p('Expand the Sources section to see exactly which chunks RAG retrieved to answer')],
    ]
    elems.append(tbl(chat_data, [0.8*inch, 5.2*inch]))
    elems.append(sp(10))

    # Demo 4
    elems.append(p('Prompt Injection Defense', H3))
    elems.append(sp(3))
    elems.append(p('Connects to: Notebooks 7, 8 — OpenAI API key required', NOTE))
    elems.append(sp(3))
    inj_data = [
        [h('Feature'), h('What It Shows')],
        [p('Attack Simulator'), p('Submit crafted prompts and see how the model responds without guardrails')],
        [p('Guardrail Toggle'),  p('Enable defenses and compare how the same attack is blocked or neutralised')],
        [p('Explanation Panel'), p('Understand why each guardrail succeeded or failed for that specific attack')],
    ]
    elems.append(tbl(inj_data, [1.5*inch, 4.5*inch]))
    return elems


def resources_page(W, M):
    elems = []
    elems.append(p('Resources and Next Steps', H2))
    elems.append(sp(6))

    # Docs index
    elems.append(p('Documentation Index', H3))
    elems.append(sp(4))
    docs_data = [
        [h('Guide'), h('File in Repo'), h('What It Covers')],
        [p('GitHub Guide'),     p('docs/github_guide.md'),     p('Forking, cloning, and downloading course materials')],
        [p('Docker Guide'),     p('docs/docker_guide.md'),     p('Installing Docker Desktop and running the container')],
        [p('OpenAI API Guide'), p('docs/openai.md'),           p('Creating an API key and understanding usage costs')],
        [p('RAG Chat Guide'),   p('docs/RAG_CHAT_GUIDE.md'),   p('Using the Estel RAG Chat demo in detail')],
        [p('Demo Guide'),       p('docs/demos_section.md'),    p('Overview of all four interactive Streamlit demos')],
    ]
    elems.append(tbl(docs_data, [1.4*inch, 1.9*inch, 2.7*inch]))
    elems.append(sp(10))

    # Next steps
    elems.append(p('Recommended Learning Sequence', H3))
    elems.append(sp(4))
    seq_data = [
        [h('Phase'), h('What To Do')],
        [p('Start free'),    p('Open notebooks 1-4 in Colab — no account or API key needed')],
        [p('Get API key'),   p('Create an OpenAI key to unlock notebooks 5-11 and all demos')],
        [p('Run demos'),     p('Install Docker Desktop and follow the 5-step setup on the previous page')],
        [p('Go deeper'),     p('Explore RAG Chat with your own documents, then try the Prompt Injection demo')],
        [p('Next level'),    p('Continue to AgenticAI Foundry for multi-agent systems, MCP, and agent security')],
    ]
    elems.append(tbl(seq_data, [1.0*inch, 5.0*inch]))
    elems.append(sp(10))

    # Getting help
    elems.append(p('Getting Help', H3))
    elems.append(sp(4))
    help_data = [
        [h('Issue'), h('Where to Look')],
        [p('Docker not starting'),     p('See docs/docker_guide.md — covers common install issues for Mac, Windows, and Linux')],
        [p('API key errors'),          p('See docs/openai.md — check for extra spaces or that your key starts with sk-')],
        [p('Colab notebook errors'),   p('Use Runtime > Restart and run all — most errors are resolved by a fresh kernel')],
        [p('Container crashes'),       p('Run: docker logs $(docker ps -lq) to see what failed at startup')],
        [p('RAG Chat not answering'),  p('Ensure your document uploaded successfully — try a smaller PDF first')],
        [p('Questions or feedback'),   p('Open an issue at: github.com/dlwhyte/GenAI_foundry/issues')],
    ]
    elems.append(tbl(help_data, [1.8*inch, 4.2*inch]))
    elems.append(sp(10))

    # Footer banner
    footer_data = [[p('Ready for the next level? Continue to AgenticAI Foundry: github.com/dlwhyte/AgenticAI_foundry', s('Ft', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=WHITE, alignment=TA_CENTER))]]
    footer = Table(footer_data, colWidths=[W - 2*M])
    footer.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    elems.append(footer)
    return elems


def build_pdf():
    output_path = 'Student_Quick_Start.pdf'
    M = 0.65 * inch
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=M, rightMargin=M,
        topMargin=0.6*inch, bottomMargin=0.6*inch,
    )
    W, H = letter

    story = []
    story += cover_page(W, M)
    story.append(PageBreak())
    story += setup_page(W, M)
    story.append(PageBreak())
    story += notebooks_page(W, M)
    story.append(PageBreak())
    story += demos_page(W, M)
    story.append(PageBreak())
    story += resources_page(W, M)

    doc.build(story)
    print(f'PDF written to {output_path}')


if __name__ == '__main__':
    build_pdf()
