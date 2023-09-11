using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AreaPerimetroFiguras
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void salirToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void operaciónToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void áreaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Deselecciona todos los elementos de menú hijos en el grupo
            foreach (ToolStripMenuItem item in operaciónToolStripMenuItem.DropDownItems)
            {
                item.Checked = false;
            }

            // Establece el elemento de menú actual como seleccionado
            ToolStripMenuItem selectedMenuItem = (ToolStripMenuItem)sender;
            selectedMenuItem.Checked = true;

            updateWindow();
        }

        private void perímetroToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Deselecciona todos los elementos de menú hijos en el grupo
            foreach (ToolStripMenuItem item in operaciónToolStripMenuItem.DropDownItems)
            {
                item.Checked = false;
            }

            // Establece el elemento de menú actual como seleccionado
            ToolStripMenuItem selectedMenuItem = (ToolStripMenuItem)sender;
            selectedMenuItem.Checked = true;

            updateWindow();
        }

        private void triánguloToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Deselecciona todos los elementos de menú hijos en el grupo
            foreach (ToolStripMenuItem item in figuraToolStripMenuItem.DropDownItems)
            {
                item.Checked = false;
            }

            // Establece el elemento de menú actual como seleccionado
            ToolStripMenuItem selectedMenuItem = (ToolStripMenuItem)sender;
            selectedMenuItem.Checked = true;

            updateWindow();
        }

        private void cuadradoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Deselecciona todos los elementos de menú hijos en el grupo
            foreach (ToolStripMenuItem item in figuraToolStripMenuItem.DropDownItems)
            {
                item.Checked = false;
            }

            // Establece el elemento de menú actual como seleccionado
            ToolStripMenuItem selectedMenuItem = (ToolStripMenuItem)sender;
            selectedMenuItem.Checked = true;

            updateWindow();
        }

        private void rectánguloToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Deselecciona todos los elementos de menú hijos en el grupo
            foreach (ToolStripMenuItem item in figuraToolStripMenuItem.DropDownItems)
            {
                item.Checked = false;
            }

            // Establece el elemento de menú actual como seleccionado
            ToolStripMenuItem selectedMenuItem = (ToolStripMenuItem)sender;
            selectedMenuItem.Checked = true;

            updateWindow();
        }

        private void círculoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Deselecciona todos los elementos de menú hijos en el grupo
            foreach (ToolStripMenuItem item in figuraToolStripMenuItem.DropDownItems)
            {
                item.Checked = false;
            }

            // Establece el elemento de menú actual como seleccionado
            ToolStripMenuItem selectedMenuItem = (ToolStripMenuItem)sender;
            selectedMenuItem.Checked = true;

            updateWindow();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void updateWindow()
        {
            string operacion = getOperacion();
            string figura = getFigura();

            // Cambia el título
            titleLabel.Text = operacion + " del " + figura;

            // Habilitar campos de entrada
            if (figura == "Triángulo")
            {
                label1.Text = "Lado 1";
                numericUpDown1.Enabled = true;

                label2.Text = "Lado 2";
                numericUpDown2.Enabled = true;

                numericUpDown3.Enabled = true;
            }
            else if (figura == "Cuadrado")
            {
                label1.Text = "Lado";
                numericUpDown1.Enabled = true;

                label2.Text = "Lado 1";
                numericUpDown2.Enabled = false;

                numericUpDown3.Enabled = false;
            }
            else if (figura == "Rectángulo") {
                label1.Text = "Largo";
                numericUpDown1.Enabled = true;

                label2.Text = "Ancho";
                numericUpDown2.Enabled = true;

                numericUpDown3.Enabled = false;
            }
            else if (figura == "Círculo")
            {
                label1.Text = "Radio";
                numericUpDown1.Enabled = true;

                label2.Text = "Lado 2";
                numericUpDown2.Enabled = false;

                numericUpDown3.Enabled = false;
            }
        }

        private String getOperacion()
        {
            foreach (ToolStripMenuItem item in operaciónToolStripMenuItem.DropDownItems)
            {
                if (item.Checked)
                {
                    return item.Text;
                }
            }

            // Valor por defecto
            return "Triángulo";
        }

        private String getFigura()
        {
            foreach (ToolStripMenuItem item in figuraToolStripMenuItem.DropDownItems)
            {
                if (item.Checked)
                {
                    return item.Text;
                }
            }

            // Valor por defecto
            return "Área";
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string operacion = getOperacion();
            string figura = getFigura();

            double a = Convert.ToDouble(numericUpDown1.Value);
            double b = Convert.ToDouble(numericUpDown2.Value);
            double c = Convert.ToDouble(numericUpDown3.Value);

            if (operacion == "Área" & figura == "Triángulo")
            {
                // Fórmula de Herón
                double s = (a + b + c) / 2; // Semiperímetro (s)
                double area = Math.Sqrt(s * (s - a) * (s - b) * (s - c));

                showResult(operacion, figura, area);
            }
            else if (operacion == "Perímetro" & figura == "Triángulo")
            {
                double perimetro = a + b + c;

                showResult(operacion, figura, perimetro);
            }
            else if (operacion == "Área" & figura == "Cuadrado")
            {
                double area = a * a;

                showResult(operacion, figura, area);
            }
            else if (operacion == "Perímetro" & figura == "Cuadrado")
            {
                double perimetro = a * 4;

                showResult(operacion, figura, perimetro);
            }
            else if (operacion == "Área" & figura == "Rectángulo")
            {
                double area = a * b;

                showResult(operacion, figura, area);
            }
            else if (operacion == "Perímetro" & figura == "Rectángulo")
            {
                double perimetro = a + a + b + b;

                showResult(operacion, figura, perimetro);
            }
            else if (operacion == "Área" & figura == "Círculo")
            {
                double area = Math.PI * Math.Pow(a, 2);

                showResult(operacion, figura, area);
            }
            else if (operacion == "Perímetro" & figura == "Círculo")
            {
                double perimetro = 2 * Math.PI * a;

                showResult(operacion, figura, perimetro);
            }
        }

        private void showResult(string operacion, string figura, double resultado)
        {
            string message = $"El {operacion.ToLower()} del {figura.ToLower()} es {resultado}";

            MessageBox.Show(message, "Resultado", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void tableLayoutPanel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void acercaDeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("github.com/meyer-pidiache", "Info");
        }
    }
}
